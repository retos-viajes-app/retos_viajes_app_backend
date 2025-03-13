from sqlalchemy import Column, Float, ForeignKey, Integer, String, TIMESTAMP, func
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from app.db.db_connection import Base
from app.db.model.category import Category

class TripCategory(Base):
    __tablename__ = 'trip_category'

    trip_id = Column(ForeignKey('trip.id'), primary_key=True)
    category_id = Column(ForeignKey('category.id'), primary_key=True)

    trip = relationship('Trip', back_populates='trip_categories')
    category = relationship('Category', back_populates='trip_categories')