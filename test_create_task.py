import sqlalchemy
import pytest
import unittest
import subprocess

from project_manager import ProjectManager
from project import Project
from model import Project as ProjectModel
from model import Task as TaskModel
from sqlalchemy import delete

from sqlalchemy.orm import Session
from database import createSession
from sqlalchemy.exc import IntegrityError

def test_create_task_valid(monkeypatch, capsys):
    session = createSession()
    firstrun = session.query(TaskModel).filter(TaskModel.task_name == "Test Task").first()
    if firstrun:
        session.delete(firstrun)
        session.commit()
    
    adjust_proj = session.query(ProjectModel).filter(ProjectModel.project_id == 1000).first()
    adjust_proj.num_of_tasks -= 1
    session.close()

    responses = iter(["Test Task", "Low", 1, "10-10-10", 0.0])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    Project.create_task(1000)

    captured = capsys.readouterr()
    captured2 = captured.out

    assert "Please enter task details: " in captured2
    assert "Task successfully created" in captured2

def test_create_task_invalid(monkeypatch, capsys):
    responses = iter(["Test Task", "Low", 1, "10-10-10", 0.0])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    Project.create_task(1000)

    captured = capsys.readouterr()
    captured2 = captured.out

    assert "Please enter task details: " in captured2
    assert "Task already exists in that project. Please use another name for that task." in captured2

