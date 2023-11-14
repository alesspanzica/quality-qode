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
    task = session.query(TaskModel).filter(TaskModel.task_num_in_project == 2, TaskModel.assigned_project == 1000).first()
    
    if task.assigned_to != "":
        task.assigned_to = ""
        session.commit()
    
    session.close()
    
    responses = iter(['alesspanzica'])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    
    ProjectManager.assign_task_to(2, 1000)

    captured = capsys.readouterr()

    assert "Task successfully assigned to alesspanzica." in captured.out

def test_assign_task_2(monkeypatch, capsys):
    session = createSession()
    task = session.query(TaskModel).filter(TaskModel.task_num_in_project == 2, TaskModel.assigned_project == 1000).first()
    
    if task.assigned_to != "":
        task.assigned_to = ""
        session.commit()
    
    session.close()
    
    responses = iter(['', 'alesspanzica'])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    
    ProjectManager.assign_task_to(2, 1000)

    captured = capsys.readouterr()

    assert "Task successfully assigned to alesspanzica." in captured.out