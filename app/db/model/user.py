# coding: utf-8
from sqlalchemy import Column, Float, ForeignKey, Integer, String, TIMESTAMP, func, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


from sqlalchemy import Column, Integer, String, TIMESTAMP, func

from app.db.db_connection import Base

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    sub = Column(String(255), unique=True, nullable=True)
    name = Column(String(50), nullable=True)
    username = Column(String(50), unique=True, nullable=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    profile_photo_url = Column(String(255))
    bio = Column(String(255))
    total_points = Column(Integer)
    auth_method = Column(String(50), nullable=False, default="google")
    hashed_password = Column(String(255), nullable=True)  # Add hashed_password column
    is_verified = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now(), onupdate=func.now())

     # Solicitudes enviadas
    connections_sent = relationship('UserConnection', back_populates='user_1')

    # Solicitudes recibidas
    connections_received = relationship('UserConnection', back_populates='user_2')
