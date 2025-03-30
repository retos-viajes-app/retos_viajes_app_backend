# coding: utf-8
from sqlalchemy import Column, Float, ForeignKey, Integer, String, TIMESTAMP, func
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from app.db.db_connection import Base


class CompletedChallenge(Base):
    __tablename__ = 'completed_challenge'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(ForeignKey('user.id', ondelete="CASCADE"), nullable=False, index=True)
    challenge_id = Column(ForeignKey('challenge.id', ondelete="CASCADE"), nullable=False, index=True)
    trip_id = Column(ForeignKey('trip.id', ondelete="CASCADE"), nullable=False, index=True)
    completed_at = Column(TIMESTAMP, default=func.now())
    proof_photo_url = Column(String(255))
    description = Column(String(255))

    challenge = relationship('Challenge')
    trip = relationship('Trip')
    user = relationship('User')