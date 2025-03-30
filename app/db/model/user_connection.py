from app.db.db_connection import Base
from sqlalchemy import Column, Float, ForeignKey, Integer, String, TIMESTAMP, func, Boolean
from sqlalchemy.orm import relationship

class UserConnection(Base):
    __tablename__ = 'user_connection'

    user_id_1 = Column(ForeignKey('user.id', ondelete="CASCADE"), primary_key=True)
    user_id_2 = Column(ForeignKey('user.id', ondelete="CASCADE"), primary_key=True)
    status = Column(String(20), default="pending")  # pending | accepted
    created_at = Column(TIMESTAMP, default=func.now())

    user_1 = relationship('User', back_populates='connections_sent', foreign_keys=[user_id_1])
    user_2 = relationship('User', back_populates='connections_received', foreign_keys=[user_id_2])