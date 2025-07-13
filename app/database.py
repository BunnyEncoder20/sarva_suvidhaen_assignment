from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# env
from app.config import settings

# defining the DB connection string
DATABASE_URL =f'postgresql://{settings.USERNAME}:{settings.PASSWORD}@{settings.HOSTNAME}:{settings.PORT}/{settings.DBNAME}'

# Creating SqlAlchemy Session to connect to Postgres DB
Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() :
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
