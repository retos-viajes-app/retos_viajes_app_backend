import random
import string
from datetime import datetime, timedelta
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.db.model.confirmation_code import ConfirmationCode
from app.db.model.user import User
from app.services.email_service import send_email

from app.auth.auth import hash_password

# Función para generar un código de recuperación de contraseña
def generate_reset_code(length=6):
    """Genera un código numérico aleatorio de la longitud especificada"""
    return ''.join(random.choices(string.digits, k=length))

# Función para crear un código de recuperación de contraseña
def create_password_reset_code(db: Session, email: str):
    user = db.query(User).filter(User.email == email).first()
    if not user:
       raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Eliminar códigos anteriores no usados
    db.query(ConfirmationCode).filter(ConfirmationCode.user_id == user.id, ConfirmationCode.used == False).delete()
    
    code = generate_reset_code()
    hashed_code = hash_password(code)
    expires_at = datetime.utcnow() + timedelta(minutes=10)
    reset_code = ConfirmationCode(user_id=user.id, code=hashed_code, expires_at=expires_at, used=False)
    try:
        db.add(reset_code)
        db.commit()
        db.refresh(reset_code)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error al generar el código")

     # Enviar correo
    subject = "Recuperación de Contraseña"
    body = f"Tu código de recuperación es: {code}\nEste código es válido por 10 minutos."
    send_email(user.email, subject, body)

    return reset_code