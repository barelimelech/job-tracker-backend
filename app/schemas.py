from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class JobApplicationBase(BaseModel):
    company_name: str
    position: str
    status: Optional[str] = "applied"
    interview_summery: Optional[str] = None

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

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: str

    class Config:
        orm_mode = True