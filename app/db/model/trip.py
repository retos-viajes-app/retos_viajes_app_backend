# coding: utf-8
from sqlalchemy import Column, Float, ForeignKey, Integer, String, TIMESTAMP, func
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app.db.model.destination import Destination
from app.db.model.user import User
from app.db.db_connection import Base


class Trip(Base):
    __tablename__ = 'trip'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(ForeignKey('user.id', ondelete="CASCADE"), nullable=False, index=True)
    destination_id = Column(ForeignKey('destination.id'), nullable=False, index=True)
    start_date = Column(TIMESTAMP, nullable=False, default=func.now())
    end_date = Column(TIMESTAMP, nullable=False, default=func.now())
    status = Column(String(100))
    created_at = Column(TIMESTAMP, default=func.now())
    destination = relationship('Destination')
    user = relationship('User')