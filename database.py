from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from user_model import Base

def createSession():
    engine = create_engine('sqlite:///user_database.db')
    Base.metadata.create_All(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
