from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


#create a database
Database_url = "postgresql://hello:1234@localhost:5432/jobmarket"

#engine to connect to the database
engine = create_engine(Database_url)

#a workplace to work with the database
SessionLocal = sessionmaker(bind=engine)

#create a parent class - foundation of database models
#models inherits from Base becomes a mapped table 
Base = declarative_base()

