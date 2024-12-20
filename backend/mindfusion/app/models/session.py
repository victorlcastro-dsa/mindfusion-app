from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database.db import Base

class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)
    tutor_id = Column(Integer, ForeignKey("tutors.id"))
    student_id = Column(Integer, ForeignKey("users.id"))
    scheduled_at = Column(DateTime, nullable=False)
    status = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    tutor = relationship("Tutor", back_populates="sessions")
    student = relationship("User", back_populates="sessions")
    review = relationship("Review", back_populates="session", uselist=False)