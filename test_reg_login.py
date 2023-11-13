from unittest.mock import patch
import pytest
from unittest import TestCase
from registration import Registration
from model import User as UserModel
from user import User
from sqlalchemy.orm import Session
from database import createSession

#Script to test if a user can register and is added to the database.
def test_register(monkeypatch, capsys):
        responses = iter(['testuser', 'testpass', 'testname', 'testnumber', 'testemail', 0,
                          0])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        Registration.register()
        captured = capsys.readouterr()
        cap = "Registration successful! Please log in.\n"
        assert captured.out == "Registration successful! Please log in.\n"

#Script to test if user can successfully login.
def test_login():
    username = "abbeycameron"
    password = "password1"

    session = createSession()
    user = session.query(UserModel).filter(UserModel.username == username).first()
    
    if user:
        assert user.password == password, "Incorrect password."
    else:
        assert user is not None, "User does not exist."

    session.close()