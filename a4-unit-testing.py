import sqlalchemy
import pytest
from unittest import TestCase
import subprocess
from project_manager import ProjectManager

def create_project(monkeypatch, capsys):
    #with mock.patch.object(builtins, 'input', lambda _: '19'):
    #    assert user_prompt() == 'Your number is 19'
    responses = iter(['MollyD', 'View', 'Exit'])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    ProjectManager.all_page()
    captured = capsys.readouterr()
    cap = "MollyD Molly Doe 6134444444 collingwood st molly@email.com 3 Sarah Mitchell\n"
    assert captured.out == "MollyD Molly Doe 6134444444 collingwood st molly@email.com 3 Sarah Mitchell\n"
    