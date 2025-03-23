from datetime import datetime
from fastapi import APIRouter, HTTPException, FastAPI, Depends
from sqlalchemy.orm import Session
from app.auth.auth import  get_current_user, verify_access_token
from app.db.model.user import User
from app.db.db_connection import get_db
from app.db.model.user_connection import UserConnection
from app.schema.user_connection import UserConnectionRequest,  UserConnectionResponse

router = APIRouter(tags=["user_connections"])

#Endpoint para realizar una solicitud de conexión a otro usuario
@router.post("/connections/request/{user_id}", response_model=dict)
def send_connection_request(user_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    # Comprobar que el usuario existe
    target_user = db.query(User).filter(User.id == user_id).first()
    if not target_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    # Comprobar que el usuario no está intentando conectarse a sí mismo
    if current_user.id == target_user.id:
        raise HTTPException(status_code=400, detail="No puedes conectar contigo mismo")

    # Verificar si ya existe una solicitud de conexión entre estos dos usuarios
    existing_connection = db.query(UserConnection).filter(
        ((UserConnection.user_id_1 == current_user.id) & (UserConnection.user_id_2 == target_user.id)) |
        ((UserConnection.user_id_1 == target_user.id) & (UserConnection.user_id_2 == current_user.id))
    ).first()

    if existing_connection:
        if existing_connection.status == "pending":
            return {
                "success": True,
                "message": "Ya existe una solicitud de conexión en estado pendiente",
                "connection_status": existing_connection.status
            }
        elif existing_connection.status == "accepted":
            return {
                "success": True,
                "message": "Ya estáis conectados",
                "connection_status": existing_connection.status
            }

    # Si no existe una conexión previa, se crea una nueva con estado "pending"
    new_connection = UserConnection(
        user_id_1=current_user.id,
        user_id_2=target_user.id,
        status="pending",
    )
    db.add(new_connection)
    db.commit()
    db.refresh(new_connection)

    return {
        "success": True,
        "message": "Solicitud de conexión enviada correctamente",
        "connection": UserConnectionResponse.model_validate(new_connection)
    }

@router.delete("/connections/request/cancel/{user_id}", response_model = dict)
def cancel_sent_connection_request(user_id : int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    existing_connection = db.query(UserConnection).filter(
        ((UserConnection.user_id_1 == current_user.id) & (UserConnection.user_id_2 == user_id))).first()
    if existing_connection is None:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")
    
    db.delete(existing_connection)
    db.commit()
    return {
        "success": True,
        "message": "Solicitud de conexión cancelada correctamente"
    }