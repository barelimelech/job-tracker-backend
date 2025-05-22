from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone
from .database import Base

class JobApplication(Base):
    __tablename__ = "job_applications"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, index=True)
    position = Column(String)
    status = Column(String, default="sent")
    application_date = Column(DateTime, default=datetime.now(timezone.utc))
