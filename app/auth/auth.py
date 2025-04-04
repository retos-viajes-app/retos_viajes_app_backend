from fastapi import HTTPException, Header
from datetime import datetime, timedelta
from pydantic import BaseModel
import os
from passlib.context import CryptContext
from jose import JWTError, jwt
from app.core.config import get_settings

ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 15
JWT_SECRET_KEY = get_settings().jwt_secret_key
JWT_REFRESH_SECRET_KEY = get_settings().jwt_refresh_secret_key
ALGORITHM = get_settings().algorithm_token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#Funcion para crear el access token
def create_access_token(user_id: str) -> str:
    expires = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub": user_id, "exp": expires}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

#Funcion para crear el refresh token
def create_refresh_token(user_id: str) -> str:
    expires = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode = {"sub": user_id, "exp": expires}
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

#Funcion para verificar el access token
def verify_access_token(authorization: str = Header(...)):
    try:
        token = authorization.split(" ")[1]  # Extraer token de "Bearer <token>"
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token payload")
        return {"sub": user_id}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid access token")


#Funciones para encriptar y verificar contraseñas
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)