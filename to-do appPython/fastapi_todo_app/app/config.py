from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
##  create_engine manages the connections to the database and executes SQL statements.
from sqlalchemy import create_engine
import os

DATABASE_URL = os.getenv("DATABASE_URL", "mysql+mysqlconnector://root:0303@localhost/todo")

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# factory function that constructs a base class for declarative class
Base = declarative_base()

def init_db():
    Base.metadata.create_all(bind=engine)


