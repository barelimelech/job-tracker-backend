from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class JobApplicationBase(BaseModel):
    company_name: str
    position: str
    status: Optional[str] = "applied"
    interview_summary: Optional[str] = None

class JobApplicationCreate(JobApplicationBase):
    pass

class JobApplicationUpdate(JobApplicationBase):
    pass

class JobApplication(JobApplicationBase):
    id: int
    application_date: datetime
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
