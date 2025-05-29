import pytest
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timezone

from app.database import Base
from app.models import JobApplication
from app.schemas import JobApplicationCreate

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)
    inspector = inspect(engine)
    print("Tables in db_session fixture:", inspector.get_table_names())

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

def test_create_job_application(db_session):
    new_job = JobApplication(
        company_name="Acme Corp",
        position="Software Engineer",
        status="applied",
        application_date=datetime.now(timezone.utc),
        interview_summery=None,
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc),
        user_id=1
    )

    db_session.add(new_job)
    db_session.commit()
    db_session.refresh(new_job)

    assert new_job.id is not None
    assert new_job.company_name == "Acme Corp"
    assert new_job.status == "applied"
    assert new_job.interview_summery == None

def test_update_job_application(db_session):
    new_job = JobApplication(
        company_name="Beta LLC",
        position="DevOps Engineer",
        status="applied",
        application_date=datetime.now(timezone.utc),
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc),
        user_id=1
    )
    db_session.add(new_job)
    db_session.commit()
    db_session.refresh(new_job)

    new_job.status = "interviewed"
    db_session.commit()
    db_session.refresh(new_job)

    assert new_job.status == "interviewed"

def test_read_job_application(db_session):
    new_job = JobApplication(
        company_name="Gamma Inc",
        position="Data Scientist",
        status="applied",
        application_date=datetime.now(timezone.utc),
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc),
        user_id=1
    )
    db_session.add(new_job)
    db_session.commit()
    db_session.refresh(new_job)

    job = db_session.query(JobApplication).filter_by(id=new_job.id).first()
    assert job is not None
    assert job.company_name == "Gamma Inc"
