from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from .database import Base

class JobApplication(Base):
    __tablename__ = "job_applications"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, index=True)
    position = Column(String)
    status = Column(String, default="sent")
    application_date = Column(DateTime, default=datetime.now(timezone.utc))
    interview_summery = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="jobs")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    jobs = relationship("JobApplication", back_populates="user")