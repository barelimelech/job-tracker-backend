# import pytest
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from fastapi.testclient import TestClient 

# from app.database import Base
# from app.main import app
# from app.routes import users

# # DB in-memory
# SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# @pytest.fixture(scope="function")
# def db_session():
#     Base.metadata.create_all(bind=engine)
#     db = TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#         Base.metadata.drop_all(bind=engine)

# @pytest.fixture(scope="function")
# def client(db_session):
#     def override_get_db():
#         try:
#             yield db_session
#         finally:
#             pass

#     app.dependency_overrides[users.get_db] = override_get_db
#     yield TestClient(app)
#     app.dependency_overrides.clear()
