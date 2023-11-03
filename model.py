'''
This file contains all the class tables for the backend.
Each class stores a different object, User, Project, or Task
'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase


#Base = declarative_base()
class Base(DeclarativeBase):
    pass
#To store user information
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

    #To assign user information
    def __init__(self, username, password, name, 
                 phone_number, address, email, position, manager):
        self.username = username
        self.password = password
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.position = position
        self.manager = manager

#To store project information
class Project(Base):
    __tablename__  = 'projects'
    
    id = Column(Integer, primary_key = True)
    project_name = Column(String, unique=True, nullable=False)
    project_id = Column(String, unique=True, nullable=False)
    deadline = Column(String)
    priority = Column(String)
    owner = Column(String)
    tasks = Column(String)

    #To assign project informaion
    def __init__(self, project_name, project_id, deadline, priority, owner, tasks):
        self.project_name=project_name
        self.project_id=project_id
        self.deadline=deadline
        self.priority=priority
        self.owner=owner
        self.tasks=tasks

#To store task information
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key = True)
    task_name = Column(String, unique=True, nullable=False)
    assigned_project = Column(String)
    priority = Column(String)
    capability_level = Column(String)
    deadline = Column(String)
    assigned_to = Column(String)
    project_portion = Column(String)

    #To assign task information
    def __init__(self, task_name, assigned_project, priority, capability_level, deadline, assigned_to, project_portion):
        self.task_name = task_name
        self.assigned_project = assigned_project
        self.priority = priority
        self.capability_level = capability_level
        self.deadline = deadline
        self.assigned_to = assigned_to
        self.project_portion = project_portion

# create all tables
#db.create_all()
'''
Add new user to database:
new_user = User(username='Sandy', email='sandy@gmail.com', password='cool-password')
session.add(new_user)
session.commit()

To retreive data:
user = session.query(User).filter_by(username="usernameEX").first()
'''