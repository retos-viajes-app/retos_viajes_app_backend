from datetime import datetime
from fastapi import APIRouter, HTTPException, FastAPI, Depends, Header, Body
from sqlalchemy.orm import Session
from app.auth.auth import create_access_token, create_refresh_token, hash_password, verify_access_token, verify_password
from app.auth.auth_google import verify_google_token
from app.db.model.user import User
from app.db.db_connection import get_db
from app.schema.password_reset import ResetPasswordRequest
from app.schema.user import  UserUpdate, UserResponse, UserLogin, UserRegister
from pydantic import BaseModel, EmailStr
from app.db.model.confirmation_code import ConfirmationCode
router = APIRouter(tags=["users"])

# Endpoint que verifica el usuario en la BD, si no existe lo crea y devuelve los tokens
#funcion especifica para google
@router.post("/verify-google-token")
def verify_google_token(db: Session = Depends(get_db), id_info: dict = Depends(verify_google_token)):
    # Buscar usuario en la base de datos por email
    db_user = db.query(User).filter(User.email == id_info['email']).first()

    if db_user is None:
        # Si el usuario no existe, lo registramos
        user_data = {
            "sub": id_info['sub'],
            "email": id_info['email'],
            "profile_photo_url": id_info.get('picture', ""),
        }
        new_user = User(**user_data)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        user_id = new_user.sub  # Usar ID recién creado

    else:
        # Si el usuario existe pero no tiene 'sub', lo actualizamos
        if db_user.sub is None:
            db_user.sub = id_info['sub']
            db.commit()
            db.refresh(db_user)

        user_id = db_user.sub  # Usar el ID del usuario existente

    # Generar tokens para el usuario
    access_token = create_access_token(user_id)
    refresh_token = create_refresh_token(user_id)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }


# Endpoint para registrar un usuario de forma tradicional
@router.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="El email ya está en uso")

    hashed_pwd = hash_password(user.password)
    new_user = User(email=user.email, hashed_password=hashed_pwd, auth_method="traditional")
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    access_token = create_access_token(str(new_user.id))
    refresh_token = create_refresh_token(str(new_user.id))

    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}

# Endpoint para hacer login de forma tradicional
@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    print("User:", user)
    print("User.userid:", user.userid)
    if "@" in user.userid:
        email = user.userid
        db_user = db.query(User).filter(User.email == email).first()
    else:
        username = user.userid
        db_user = db.query(User).filter(User.username == username).first()
        
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")

    access_token = create_access_token(str(db_user.id))
    refresh_token = create_refresh_token(str(db_user.id))

    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}

# Endpoint para obtener un usuario por email o username
@router.get("/users/{identifier}", response_model=UserResponse)
def get_user(identifier: str, db: Session = Depends(get_db), idinfo: dict = Depends(verify_access_token)):
    # Verificar si el identificador es un email o un username
    if "@" in identifier:  # Si contiene "@", asumimos que es un email
        db_user = db.query(User).filter(User.email == identifier).first()
    else:  # De lo contrario, lo tratamos como username
        db_user = db.query(User).filter(User.username == identifier).first()

    if db_user is None:
        raise HTTPException(status_code=404, detail="No se encontró el usuario")

    return db_user


# Endpoint para actualizar un usuario por email
@router.put("/users/{email}", response_model=UserResponse)
def update_user(email: str, user_update: UserUpdate, db: Session = Depends(get_db), idinfo: dict = Depends(verify_access_token)):
    # Obtener el usuario actual por email
    db_user = db.query(User).filter(User.email == email).first()
    
    if db_user is None:
        raise HTTPException(status_code=404, detail="No se encontró el usuario")

    # Verificar si el nuevo username ya está en uso
    if user_update.username:
        existing_user = db.query(User).filter(User.username == user_update.username).first()
        if existing_user and existing_user.email != email:
            raise HTTPException(status_code=400, detail="El nombre de usuario ya está en uso")

    # Actualizar los campos permitidos
    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)
    return db_user


# Endpoint para eliminar un usuario por email
@router.delete("/users/{email}", response_model=UserResponse)
def delete_user(email: str, db: Session = Depends(get_db), idinfo: dict = Depends(verify_access_token)):
    db_user = db.query(User).filter(User.email == email).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="No se encontró el usuario")

    db.delete(db_user)
    db.commit()
    return db_user



@router.post("/users/reset-password/{email}")
def reset_password(email: str, data: ResetPasswordRequest, db: Session = Depends(get_db)):
    print("email:", email)
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    reset_code = db.query(ConfirmationCode).filter(
        ConfirmationCode.user_id == user.id,
        ConfirmationCode.used == False,
       ConfirmationCode.expires_at > datetime.utcnow()
    ).first()

    if not reset_code or (reset_code and not verify_password(data.code, reset_code.code)):
        raise HTTPException(status_code=400, detail="Código de recuperación no válido o expirado")
    
    user.hashed_password = hash_password(data.new_password)
    reset_code.used = True

    db.commit()
    
    return {"message": "Contraseña actualizada correctamente"}