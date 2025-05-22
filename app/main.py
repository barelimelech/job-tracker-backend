from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/jobs/", response_model=schemas.JobApplication)
def create_job(job: schemas.JobApplicationCreate, db: Session = Depends(get_db)):
    return crud.create_job_application(db=db, job=job)

@app.get("/jobs/", response_model=list[schemas.JobApplication])
def read_jobs(db: Session = Depends(get_db)):
    return crud.get_all_jobs(db)
