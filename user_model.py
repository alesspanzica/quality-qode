from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

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

    def __init__(self, username, password, name, 
                 phone_number, address, email, position, manager):
        self.username = username
        self.password = password
        self.anme = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.position = position
        self.manager = manager



'''
Add new user to database:
new_user = User(username='Sandy', email='sandy@gmail.com', password='cool-password')
session.add(new_user)
session.commit()

To retreive data:
user = session.query(User).filter_by(username="usernameEX").first()
'''