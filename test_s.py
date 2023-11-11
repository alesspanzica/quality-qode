import sqlalchemy
import pytest
from unittest import TestCase
import subprocess
from user_profile import Profile

def test_answer(monkeypatch, capsys):
    #with mock.patch.object(builtins, 'input', lambda _: '19'):
    #    assert user_prompt() == 'Your number is 19'
    responses = iter(['MollyD', 'View', 'Exit'])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    Profile.all_page()
    captured = capsys.readouterr()
    cap = "MollyD Molly Doe 6134444444 collingwood st molly@email.com 3 Sarah Mitchell\n"
    assert captured.out == "MollyD Molly Doe 6134444444 collingwood st molly@email.com 3 Sarah Mitchell\n"

def test_answer2 (monkeypatch, capsys):
    responses = iter(['Cameron', 'Edit', 'name', 'Cameron', 'Exit'])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    captured = capsys.readouterr()
    Profile.all_page()
    captured = capsys.readouterr()
    assert captured.out == "Cameron Cameron 6137777777 union st louis@email.con 2 Samuel Patel\n"
