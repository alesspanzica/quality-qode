from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base

engine = create_engine('sqlite:///user_database.db')
Base.metadata.create_all(engine)
#Session = sessionmaker(bind=engine)

def createSession():
    Session = sessionmaker(bind=engine)
    return Session()
