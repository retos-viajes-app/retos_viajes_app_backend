from sqlalchemy import Column, Float, ForeignKey, Integer, String, TIMESTAMP, func
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app.db.db_connection import Base

from app.db.model.challenge import Challenge


class TripChallenge(Base):
    __tablename__ = 'trip_challenge'

    trip_id = Column(ForeignKey('trip.id'), primary_key=True)
    challenge_id = Column(ForeignKey('challenge.id'), primary_key=True)

    trip = relationship('Trip', back_populates='trip_challenges')
    challenge = relationship('Challenge', back_populates='trip_challenges')