'''
This file contains all the class tables for the backend.
Each class stores a different object, User, Project, or Task
'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase


#Creat declarative base
class Base(DeclarativeBase):
    pass

#To store user information
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key = True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, unique=False, nullable=False)
    name = Column(String, unique=False, nullable=False)
    phone_number = Column(String, unique=True, nullable=False)
    address = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
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
    deadline = Column(String, unique=False, nullable=False)
    priority = Column(String, unique=False, nullable=False)
    owner = Column(String, unique=False, nullable=False)
    num_of_tasks = Column(Integer, unique=False, nullable=False)

    #To assign project informaion
    def __init__(self, project_name, project_id, deadline, priority, owner, num_of_tasks):
        self.project_name=project_name
        self.project_id=project_id
        self.deadline=deadline
        self.priority=priority
        self.owner=owner
        self.num_of_tasks=num_of_tasks

#To store task information
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key = True)
    task_name = Column(String, unique=True, nullable=False)
    assigned_project = Column(String, unique=False, nullable=False)
    priority = Column(String, unique=False, nullable=False)
    capability_level = Column(String, unique=False, nullable=False)
    deadline = Column(String, unique=False, nullable=False)
    assigned_to = Column(String, unique=False, nullable=False)
    task_num_in_project = Column(Integer, unique=False, nullable=False )
    project_portion = Column(String, unique=False, nullable=False)

    """
    __init__(...): Paramaterized constructor for the Task class. When called, it initializes the 
                   of the Task() object and stores the provided variables correspondingly.
    
    parameters:
        all the attributes described at the top of this class (see comment above)

    """
    def __init__(self, task_name, assigned_project, priority, capability_level, deadline, task_num_in_project, project_portion):
        self.task_name = task_name
        self.assigned_project = assigned_project
        self.priority = priority
        self.capability_level = capability_level
        self.deadline = deadline
        self.assigned_to = ""
        self.task_num_in_project = task_num_in_project
        self.project_portion = project_portion