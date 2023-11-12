import sqlalchemy
import pytest
from unittest import TestCase
import subprocess
from user_profile import Profile

def test_answer(monkeypatch, capsys):
    #with mock.patch.object(builtins, 'input', lambda _: '19'):
    #    assert user_prompt() == 'Your number is 19'
    responses = iter(['mollyd', 'View', 'Exit'])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    Profile.all_page()
    captured = capsys.readouterr()
    cap = "mollyd Molly Doe 6134444444 1 Collingwood St molly@email.com 2 Olivia Wilson\n"
    assert captured.out == "mollyd Molly Doe 6134444444 1 Collingwood St molly@email.com 2 Olivia Wilson\n"

def test_answer2 (monkeypatch, capsys):
    responses = iter(['cameronj', 'Edit', 'name', 'Cameron John', 'Exit'])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    captured = capsys.readouterr()
    Profile.all_page()
    captured = capsys.readouterr()
    assert captured.out == "cameronj Cameron John 6137777777 4 Alfred St louis@email.com 5 Samuel Patel\n"
