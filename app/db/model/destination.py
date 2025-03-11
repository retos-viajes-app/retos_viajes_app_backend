# coding: utf-8
from sqlalchemy import Column, Float, ForeignKey, Integer, String, TIMESTAMP, func
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from app.db.db_connection import Base



class Destination(Base):
    __tablename__ = 'destination'

    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String(100), nullable=False)
    country = Column(String(100), nullable=False)
    description = Column(String(255))
    image_url = Column(String(255))
    active = Column(TINYINT(1))
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now(), onupdate=func.now())