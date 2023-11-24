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

# BASIC BLOCK 1 - entire project function success
def test_create_task_b1(monkeypatch, capsys):
    session = createSession()
    firstrun = session.query(TaskModel).filter(TaskModel.task_name == "Test Task").first()
    adjust_proj = session.query(ProjectModel).filter(ProjectModel.project_id == 1000).first()
    if firstrun:
        session.delete(firstrun)
        adjust_proj.num_of_tasks = adjust_proj.num_of_tasks - 1
        session.commit()
    
    session.close()

    responses = iter(["Test Task", "Low", 1, "10-10-10", 0.0])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    Project.create_task(1000)

    captured = capsys.readouterr()
    captured2 = captured.out

    assert "Please enter task details: " in captured2
    assert "Task successfully created" in captured2

# BASIC BLOCK 2 - invalid name input and goes into else (task creation success)
def test_create_task_b2(monkeypatch, capsys):
    session = createSession()
    firstrun = session.query(TaskModel).filter(TaskModel.task_name == "Test Task").first()
    adjust_proj = session.query(ProjectModel).filter(ProjectModel.project_id == 1000).first()
    if firstrun:
        session.delete(firstrun)
        adjust_proj.num_of_tasks = adjust_proj.num_of_tasks - 1
        session.commit()
    
    session.close()

    responses = iter(["", "Test Task", "Low", 1, "10-10-10", 0.0])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    Project.create_task(1000)

    captured = capsys.readouterr()
    captured2 = captured.out

    assert "Please enter task details: " in captured2
    assert "   You need to enter a valid task name. Try again: " in captured2
    assert "Task successfully created" in captured2

# BASIC BLOCK 3 - valid input and goes into if (task already exists)
def test_create_task_b3(monkeypatch, capsys):
    responses = iter(["Test Task", "Low", 1, "10-10-10", 0.0])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    Project.create_task(1000)

    captured = capsys.readouterr()
    captured2 = captured.out

    assert "Please enter task details: " in captured2
    assert "Task already exists in that project. Please use another name for that task." in captured2

# BASIC BLOCK 4 - missing initial field and goes into if (task already exists)
def test_does_task_b4(monkeypatch, capsys):
    responses = iter(["", "Test Task", "Low", 1, "10-10-10", 0.0])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    Project.create_task(1000)

    captured = capsys.readouterr()
    captured2 = captured.out

    assert "Please enter task details: " in captured2
    assert "   You need to enter a valid task name. Try again: " in captured2
    assert "Task already exists in that project. Please use another name for that task." in captured2

    
session = createSession()
#delete task to restore database
task = session.query(TaskModel).filter(TaskModel.task_name == "Test Task").first()
session.delete(task)

#reset num of tasks back to original value
adjust_proj = session.query(ProjectModel).filter(ProjectModel.project_id == 1000).first()
adjust_proj.num_of_tasks = adjust_proj.num_of_tasks - 1

session.commit()
session.close()
