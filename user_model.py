from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key = True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String)
    phone_number = Column(String)
    address = Column(String)
    email = Column(String)
    position = Column(String)
    manager = Column(String)



'''
Add new user to database:
new_user = User(username='Sandy', email='sandy@gmail.com', password='cool-password')
session.add(new_user)
session.commit()

To retreive data:
user = session.query(User).filter_by(username="usernameEX").first()
'''