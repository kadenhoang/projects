from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


#create a database
Database_url = "postgresql://postgres:password@localhost:5432/jobmarket"

#engine to connect to the database
engine = create_engine(Database_url)

#a workplace to work with the database
SessionLocal = sessionmaker(bind=engine)

#create a parent class
Base = declarative_base()