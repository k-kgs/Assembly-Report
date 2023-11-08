from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from service_config.settings import settings

DATABASE_URL: str = settings.DATABASE_URL

database_engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=database_engine) 
Base = declarative_base()

def create_tables():
    Base.metadata.create_all(bind=database_engine)