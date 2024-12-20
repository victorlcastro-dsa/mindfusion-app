from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database.db import Base

class Tutor(Base):
    __tablename__ = "tutors"

    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    specialization = Column(String, nullable=False)
    price_per_hour = Column(Float, nullable=False)
    bio = Column(String)
    availability = Column(String)

    user = relationship("User", back_populates="tutor")
    sessions = relationship("Session", back_populates="tutor")
    reviews = relationship("Review", back_populates="tutor")