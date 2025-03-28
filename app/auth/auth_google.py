from google.oauth2 import id_token
from google.auth.transport import requests as google_request
from fastapi import HTTPException, Header
from app.core.config import get_settings

WEB_CLIENT_ID = get_settings().web_client_id

#Funcion para verificar el token de Google
def verify_google_token(authorization: str = Header(...)):
    try:
        token = authorization.split(" ")[1]  # Extraer token de "Bearer <token>"
        # Verificar el token con Google
        id_info = id_token.verify_oauth2_token(
            token, 
            google_request.Request(), 
            WEB_CLIENT_ID
        )

        # Verificar que el token proviene de Google
        if id_info['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Invalid issuer')

        # Devuelve solo los datos esenciales
        return {"sub": id_info.get("sub"), "email": id_info.get("email"), "picture": id_info.get("picture")}

    except ValueError as e:
        print(f"Error validando token: {str(e)}")
        raise HTTPException(status_code=401, detail=f"Invalid token: {str(e)}")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")
        raise HTTPException(status_code=401, detail=str(e))