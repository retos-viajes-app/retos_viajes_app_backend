from datetime import datetime
from fastapi import APIRouter, HTTPException, FastAPI, Depends
from sqlalchemy.orm import Session
from app.auth.auth import  get_current_user, verify_access_token
from app.db.model.user import User
from app.db.db_connection import get_db
from app.db.model.user_connection import UserConnection

router = APIRouter(tags=["user_connections"])

@router.post("/connections/request/{user_id}")
def send_connection_request(user_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    # Comprobar que el usuario existe
    target_user = db.query(User).filter(User.id == user_id).first()
    if not target_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    # Comprobar que el usuario no está intentando conectarse a sí mismo
    if current_user.id == target_user.id:
        raise HTTPException(status_code=400, detail="No puedes conectar contigo mismo")

    # Verificar si ya existe una solicitud pendiente de conexión entre estos dos usuarios
    existing_connection = db.query(UserConnection).filter(
        ((UserConnection.user_id_1 == current_user.id) & (UserConnection.user_id_2 == target_user.id)) |
        ((UserConnection.user_id_1 == target_user.id) & (UserConnection.user_id_2 == current_user.id))
    ).first()

    if existing_connection:
        if existing_connection.status == "pending":
            raise HTTPException(status_code=400, detail="La solicitud de conexión ya se ha enviado")
        elif existing_connection.status == "accepted":
            raise HTTPException(status_code=400, detail="Ya has conectado con ese usuario")
    

    # Crear una nueva conexión con status pending
    new_connection = UserConnection(
        user_id_1=current_user.id,
        user_id_2=target_user.id,
        status="pending",
    )
    db.add(new_connection)
    db.commit()
    db.refresh(new_connection)

    return {"message": "Solicitud de conexión enviada correctamente", "success": True}