# coding: utf-8
from sqlalchemy import Column, Float, ForeignKey, Integer, String, TIMESTAMP, func
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from app.db.db_connection import Base


class Challenge(Base):
    __tablename__ = 'challenge'

    id = Column(Integer, primary_key=True, autoincrement=True)
    category_id = Column(ForeignKey('category.id'), nullable=False, index=True)
    destination_id = Column(ForeignKey('destination.id'), nullable=False, index=True)
    title = Column(String(100), nullable=False)
    short_description = Column(String(100), nullable=False)
    long_description = Column(String(255))
    image_url = Column(String(255))
    points = Column(Integer, nullable=False)
    difficulty = Column(Integer)
    active = Column(TINYINT(1))
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now(), onupdate=func.now())
    latitude = Column(Float(asdecimal=True))
    longitude = Column(Float(asdecimal=True))

    category = relationship('Category')
    destination = relationship('Destination')