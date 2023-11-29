from unittest.mock import patch
import pytest
from unittest import TestCase
from registration import Registration
from model import User as UserModel
from sqlalchemy import delete
from user import User
from sqlalchemy.orm import Session
from database import createSession
from project_manager import ProjectManager
from project import Project
from model import Project as ProjectModel
from model import Task as TaskModel
from sqlalchemy import delete
from sqlalchemy.exc import IntegrityError

'''PATH 1: 1->2->3 
Empty project name input for project variable then
enter existing project name for project varaible.
Checks for incorrect inputs.
'''
def test_path_123(monkeypatch, capsys):
    #session = createSession()
    empty = " ".strip()
    responses = iter(["", "Test Project2", "9877", "01-01-0001", "Low", "Jim"])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    ProjectManager.create_project()
    captured = capsys.readouterr()
    captured2 = captured.out
    # Check if the expected messages are in the captured output
    assert "You must enter a name." in captured2
    assert "Project already exists. Try again." in captured2

'''PATH 2: 1->3 
Enter existing project name for project variable. 
Checks for incorrect inputs.
 '''
def test_path_13(monkeypatch, capsys):
    responses = iter(["Test Project2", "9877", "01-01-0001", "Low", "Jim"])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    ProjectManager.create_project()
    captured = capsys.readouterr()
    captured2 = captured.out
    # Check if the expected messages are in the captured output
    assert "Project already exists. Try again." in captured2

'''PATH 3: 1->2->4 
Enter empty project name then enter successful new project name for project variable
Checks for incorrect and then a correct input.
'''
def test_path_124(monkeypatch, capsys):
    session = createSession()
    firstrun = session.query(ProjectModel).filter(ProjectModel.project_name == "Test Project2").first()
    if firstrun:
        session.delete(firstrun)
        session.commit()
    session.close()
    responses = iter(["", "Test Project2", "9877", "01-01-0001", "Low", "Jim"])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    ProjectManager.create_project()
    captured = capsys.readouterr()
    captured2 = captured.out
    # Check if the expected messages are in the captured output
    assert "You must enter a name." in captured2
    assert "Project created successfully." in captured2


'''PATH 4: 1->4 
Enter successful new project name.
Checks for correct input.
'''
def test_path_14(monkeypatch, capsys):
    session = createSession()
    firstrun = session.query(ProjectModel).filter(ProjectModel.project_name == "Test Project2").first()
    if firstrun:
        session.delete(firstrun)
        session.commit()
    session.close()
    responses = iter(["Test Project2", "9877", "01-01-0001", "Low", "Jim"])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    ProjectManager.create_project()
    captured = capsys.readouterr()
    captured2 = captured.out
    # Check if the expected messages are in the captured output
    assert "Project created successfully." in captured2
