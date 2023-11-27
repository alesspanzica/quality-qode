import sqlalchemy
import pytest
from unittest import TestCase
import subprocess
from project_manager import ProjectManager

def test_assign_task_1(monkeypatch, capsys):
    responses = iter(['alesspanzica', '1', 'A', 'alesspanzica'])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    ProjectManager.print_projects()
    captured = capsys.readouterr()
    cap = "Task successfully assigned to alesspanzica.\n"
    assert captured.out == "Task successfully assigned to alesspanzica.\n"

def test_assign_task_2(monkeypatch, capsys):
    responses = iter(['alesspanzica', '1', 'A', 'alesspanzica'])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    ProjectManager.print_projects()
    captured = capsys.readouterr()
    cap = "Task successfully assigned to alesspanzica.\n"
    assert captured.out == "Task successfully assigned to alesspanzica.\n"
    