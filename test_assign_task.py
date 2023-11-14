import sqlalchemy
import pytest
from unittest import TestCase
import subprocess
from project_manager import ProjectManager
from model import Task as TaskModel
from sqlalchemy import delete

from sqlalchemy.orm import Session
from database import createSession

def test_assign_task_1(monkeypatch, capsys):
    session = createSession()
    task = session.query(TaskModel).filter(TaskModel.task_name == "Develop Profile Page").first()
    
    if task.assigned_to is not "":
        task.assigned_to = ""
        session.commit()
    
    session.close()
    
    responses = iter(['A', 'alesspanzica'])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    
    ProjectManager.print_task_details(task)

    captured = capsys.readouterr()
    captured2 = captured.out

    assert "Please enter your username to view all team projects: " in captured2
    assert "Task successfully assigned to alessiapanzica." in captured2

def test_assign_task_2(monkeypatch, capsys):
    responses = iter(['alesspanzica', '1', 'A', 'alesspanzica'])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    
    ProjectManager.print_projects()

    captured = capsys.readouterr()
    cap = "Task successfully assigned to alesspanzica.\n"
    assert captured.out == "Task successfully assigned to alesspanzica.\n"
    