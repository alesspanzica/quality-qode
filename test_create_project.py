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


def test_create_project_valid(monkeypatch, capsys):
    session = createSession()
    firstrun = session.query(ProjectModel).filter(ProjectModel.project_name == "Test Project").first()
    if firstrun:
        session.delete(firstrun)
        session.commit()
    session.close()

    responses = iter(["Test Project", "9876", "01-01-01", "Low", "Samuel Patel"])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    ProjectManager.create_project()

    captured = capsys.readouterr()
    captured2 = captured.out

    # Check if the expected messages are in the captured output
    assert "Please enter Project details: " in captured2
    assert "Project created successfully." in captured2

def test_create_project_invalid(monkeypatch, capsys):
    responses = iter(["Test Project", "9876", "01-01-01", "Low", "Samuel Patel"])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    ProjectManager.create_project()

    captured = capsys.readouterr()
    captured2 = captured.out

    # Check if the expected messages are in the captured output
    assert "Please enter Project details: " in captured2
    assert "Project already exists. Try again." in captured2

def test_create_project_missing(monkeypatch, capsys):
    session = createSession()
    firstrun = session.query(ProjectModel).filter(ProjectModel.project_name == "Test Project").first()
    if firstrun:
        session.delete(firstrun)
        session.commit()
    session.close()

    responses = iter(["", "Test Project", "9876", "01-01-01", "Low", "Samuel Patel"])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    ProjectManager.create_project()

    captured = capsys.readouterr()
    captured2 = captured.out

    # Check if the expected messages are in the captured output
    assert "Please enter Project details: " in captured2
    assert "You must enter a name." in captured2
    assert "Project created successfully." in captured2

def test_faketest():
    session = createSession()
    project = session.query(ProjectModel).filter(ProjectModel.project_name == "Test Project").first()
    session.delete(project)
    session.commit()
    session.close()