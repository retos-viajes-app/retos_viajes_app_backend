from datetime import datetime
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth.auth import hash_password, verify_password
from app.schema.confirmation_code import VerifyConfirmationCode
from app.db.model.user import User
from app.services.reset_password import create_password_reset_code
from app.db.db_connection import get_db
from fastapi import APIRouter
from app.schema.user import UserEmail
from app.db.model.confirmation_code import ConfirmationCode
router = APIRouter(tags=["confirmation_codes"])


# Endpoint para solicitar un código de recuperación
@router.post("/confirmation-code/request")
def request_confirmation_code(data: UserEmail, db: Session = Depends(get_db)):
    try:
        reset_code = create_password_reset_code(db, data.email)
        return {"message": "Código de confirmación enviado", "success": True}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al enviar el correo: {str(e)}")
    
# Endpoint para verificar el código de recuperación
@router.post("/confirmation-code/verify")
def verify_confirmation_code(data: VerifyConfirmationCode, db: Session = Depends(get_db)):
    
    user = db.query(User).filter(User.email == data.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
   
        
    reset_code = db.query(ConfirmationCode).filter(
        ConfirmationCode.user_id == user.id,
        ConfirmationCode.used == False,
        ConfirmationCode.expires_at > datetime.utcnow()
    ).first()

    

    if not reset_code:
        raise HTTPException(status_code=400, detail="Código de recuperación no válido o expirado")
    
    if not verify_password(data.code, reset_code.code):
        raise HTTPException(status_code=400, detail="Código incorrecto")
    
    if data.is_registration:
        user.is_verified = True
        reset_code.used = True
        db.commit()
    
    return {"message": "Código verificado correctamente", "success": True}

