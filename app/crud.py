from sqlalchemy.orm import Session
from . import models, schemas

def create_job_application(db: Session, job: schemas.JobApplicationCreate):
    db_job = models.JobApplication(**job.model_dump())
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

def get_all_jobs(db: Session):
    return db.query(models.JobApplication).all()
