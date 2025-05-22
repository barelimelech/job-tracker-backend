from pydantic import BaseModel
from datetime import datetime

class JobApplicationBase(BaseModel):
    company_name: str
    position: str
    status: str = "sent"

class JobApplicationCreate(JobApplicationBase):
    pass

class JobApplication(JobApplicationBase):
    id: int
    application_date: datetime

    class Config:
        orm_mode = True
