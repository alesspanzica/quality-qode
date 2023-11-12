from unittest.mock import patch
import pytest
from unittest import TestCase
from registration import Registration
from model import User as UserModel
from user import User
from sqlalchemy.orm import Session
from database import createSession

#Script to test if a user can register and is added to the database.
def test_register(monkeypatch):
    session = createSession()
    def mock_register(username, name, number, address, email, 
                      position, manager, password):
        test_user = UserModel(username, name, number, address, email, 
                      position, manager, password)
        session.add(test_user)
        #session.commit()

    monkeypatch.setattr('registration.Registration.register', mock_register)
    
    #Creating a user to test
    test_username = "testuser"
    test_name = "testname"
    test_number = "testnum"
    test_add = "testadd"
    test_email = "testemail"
    test_pos = "test_pos"
    test_manager = "test_manager"
    test_pass = "testpass"

    results = Registration.register(test_username, test_name, test_number, test_add,
                       test_email, test_pos, test_manager, test_pass)
    
    assert results, "Registration failed"

    test_user1 = session.query(UserModel).filter(UserModel.username == test_username). first()
    session.close()

    assert test_user1 is not None, "User was not registered"

#Script to test if user can successfully login.
def test_login():
    username = "MollyD"
    password = "password1"

    session = createSession()
    user = session.query(UserModel).filter(UserModel.username == username).first()
    
    if user:
        assert user.password == password, "Incorrect password."
    else:
        assert user is not None, "User does not exist."

    session.close()