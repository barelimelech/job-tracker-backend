from sqlalchemy.orm import Session
from . import models, schemas

def create_job_application(db: Session, job: schemas.JobApplicationCreate):
    db_job = models.JobApplication(**job.dict())
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

# שליפת כל המשרות מהמסד (READ)
def get_all_jobs(db: Session):
    return db.query(models.JobApplication).all()
