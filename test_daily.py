import sqlalchemy
import pytest
from unittest import TestCase
import subprocess
from project_manager import ProjectManager
from model import Task as TaskModel
from sqlalchemy import delete
from user_profile import Profile
from sqlalchemy.orm import Session
from database import createSession
from sqlalchemy.exc import IntegrityError
from unittest.mock import patch
from registration import Registration
from model import User as UserModel
from user import User
from project import Project
from model import Project as ProjectModel

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

def test_faketestproj():
    session = createSession()
    project = session.query(ProjectModel).filter(ProjectModel.project_name == "Test Project").first()
    session.delete(project)
    session.commit()
    session.close()

def test_create_task_valid(monkeypatch, capsys):
    session = createSession()
    firstrun = session.query(TaskModel).filter(TaskModel.task_name == "Test Task").first()
    adjust_proj = session.query(ProjectModel).filter(ProjectModel.project_id == 1000).first()
    if firstrun:
        session.delete(firstrun)
        adjust_proj.num_of_tasks = adjust_proj.num_of_tasks - 1
        session.commit()
    
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

def test_create_task_missing(monkeypatch, capsys):
    session = createSession()
    firstrun = session.query(TaskModel).filter(TaskModel.task_name == "Test Task").first()
    adjust_proj = session.query(ProjectModel).filter(ProjectModel.project_id == 1000).first()
    if firstrun:
        session.delete(firstrun)
        adjust_proj.num_of_tasks = adjust_proj.num_of_tasks - 1
        session.commit()
    
    session.close()

    responses = iter(["", "Test Task", "Low", 1, "10-10-10", 0.0])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    Project.create_task(1000)

    captured = capsys.readouterr()
    captured2 = captured.out

    assert "Please enter task details: " in captured2
    assert "   You need to enter a valid task name." in captured2
    assert "Task successfully created" in captured2


def test_does_task_num_update(monkeypatch, capsys):
    session = createSession()
    firstrun = session.query(TaskModel).filter(TaskModel.task_name == "Test Task").first()
    adjust_proj = session.query(ProjectModel).filter(ProjectModel.project_id == 1000).first()
    if firstrun:
        session.delete(firstrun)
        adjust_proj.num_of_tasks = adjust_proj.num_of_tasks - 1
        session.commit()

    responses = iter(["Test Task", "Low", 1, "10-10-10", 0.0])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    Project.create_task(1000)

    captured = capsys.readouterr()
    captured2 = captured.out

    created_task = session.query(TaskModel).filter(TaskModel.task_name == "Test Task").first()
    if created_task.task_num_in_project == adjust_proj.num_of_tasks:
        assert True
    else:
        assert False
    assert "Please enter task details: " in captured2
    assert "Task successfully created" in captured2
    session.close()



def test_path_123(monkeypatch, capsys):
    #session = createSession()
    empty = " ".strip()
    responses = iter(["", "Test Project2", "9877", "01-01-0001", "Low", "Jim"])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    ProjectManager.create_project()
    captured = capsys.readouterr()
    captured2 = captured.out
    # Check if the expected messages are in the captured output
    assert "You must enter a name." in captured2
    assert "Project already exists. Try again." in captured2

'''PATH 2: 1->3 
Enter existing project name for project variable. 
Checks for incorrect inputs.
 '''
def test_path_13(monkeypatch, capsys):
    responses = iter(["Test Project2", "9877", "01-01-0001", "Low", "Jim"])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    ProjectManager.create_project()
    captured = capsys.readouterr()
    captured2 = captured.out
    # Check if the expected messages are in the captured output
    assert "Project already exists. Try again." in captured2

'''PATH 3: 1->2->4 
Enter empty project name then enter successful new project name for project variable
Checks for incorrect and then a correct input.
'''
def test_path_124(monkeypatch, capsys):
    session = createSession()
    firstrun = session.query(ProjectModel).filter(ProjectModel.project_name == "Test Project2").first()
    if firstrun:
        session.delete(firstrun)
        session.commit()
    session.close()
    responses = iter(["", "Test Project2", "9877", "01-01-0001", "Low", "Jim"])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    ProjectManager.create_project()
    captured = capsys.readouterr()
    captured2 = captured.out
    # Check if the expected messages are in the captured output
    assert "You must enter a name." in captured2
    assert "Project created successfully." in captured2


'''PATH 4: 1->4 
Enter successful new project name.
Checks for correct input.
'''
def test_path_14(monkeypatch, capsys):
    session = createSession()
    firstrun = session.query(ProjectModel).filter(ProjectModel.project_name == "Test Project2").first()
    if firstrun:
        session.delete(firstrun)
        session.commit()
    session.close()
    responses = iter(["Test Project2", "9877", "01-01-0001", "Low", "Jim"])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    ProjectManager.create_project()
    captured = capsys.readouterr()
    captured2 = captured.out
    # Check if the expected messages are in the captured output
    assert "Project created successfully." in captured2

#Script to test if a user can register and is added to the database.
def test_register(monkeypatch, capsys):
        session = createSession()
        firsttime = session.query(UserModel).filter(UserModel.username == "testpass")
        if firsttime:
            stmt = delete(UserModel).where(UserModel.username == "testpass")
        session.close()
        responses = iter(['testuser', 'testpass', 'testname', 'testnumber', 'testemail', 
                          '0', "test2","0"])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        Registration.register()
        captured = capsys.readouterr()
        captured2 = []
        for i in range(40,0, -1):
            captured2 += captured.out[-i]
        captured2 = ''.join(captured2)
        assert captured2 == "Registration successful! Please log in.\n"

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

def test_answer3 (monkeypatch, capsys):
    responses = iter(['nonsense', 'Exit'])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    captured = capsys.readouterr()
    Profile.all_page()
    captured = capsys.readouterr()
    assert captured.out == "Unrecognized Input.\n", "Unrecognized Input"

# BASIC BLOCK 1 - entire project function success
def test_create_task_b1(monkeypatch, capsys):
    session = createSession()
    firstrun = session.query(TaskModel).filter(TaskModel.task_name == "Test Task").first()
    adjust_proj = session.query(ProjectModel).filter(ProjectModel.project_id == 1000).first()
    if firstrun:
        session.delete(firstrun)
        adjust_proj.num_of_tasks = adjust_proj.num_of_tasks - 1
        session.commit()
    
    session.close()

    responses = iter(["Test Task", "Low", 1, "10-10-10", 0.0])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    Project.create_task(1000)

    captured = capsys.readouterr()
    captured2 = captured.out

    assert "Please enter task details: " in captured2
    assert "Task successfully created" in captured2

# BASIC BLOCK 2 - invalid name input and goes into else (task creation success)
def test_create_task_b2(monkeypatch, capsys):
    session = createSession()
    firstrun = session.query(TaskModel).filter(TaskModel.task_name == "Test Task").first()
    adjust_proj = session.query(ProjectModel).filter(ProjectModel.project_id == 1000).first()
    if firstrun:
        session.delete(firstrun)
        adjust_proj.num_of_tasks = adjust_proj.num_of_tasks - 1
        session.commit()
    
    session.close()

    responses = iter(["", "Test Task", "Low", 1, "10-10-10", 0.0])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    Project.create_task(1000)

    captured = capsys.readouterr()
    captured2 = captured.out

    assert "   You need to enter a valid task name." in captured2
    assert "Task successfully created" in captured2

# BASIC BLOCK 3 - valid input and goes into if (task already exists)
def test_create_task_b3(monkeypatch, capsys):
    responses = iter(["Test Task", "Low", 1, "10-10-10", 0.0])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    Project.create_task(1000)

    captured = capsys.readouterr()
    captured2 = captured.out

    assert "Please enter task details: " in captured2
    assert "Task already exists in that project. Please use another name for that task." in captured2

# BASIC BLOCK 4 - missing initial field and goes into if (task already exists)
def test_does_task_b4(monkeypatch, capsys):
    responses = iter(["", "Test Task", "Low", 1, "10-10-10", 0.0])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    Project.create_task(1000)

    captured = capsys.readouterr()
    captured2 = captured.out

    assert "   You need to enter a valid task name." in captured2
    assert "Task already exists in that project. Please use another name for that task." in captured2


# not included in the testing - restores the database
def test_faketesttask():    
    session = createSession()
    #delete task to restore database
    task = session.query(TaskModel).filter(TaskModel.task_name == "Test Task").first()
    session.delete(task)

    #reset num of tasks back to original value
    adjust_proj = session.query(ProjectModel).filter(ProjectModel.project_id == 1000).first()
    adjust_proj.num_of_tasks = adjust_proj.num_of_tasks - 1

    session.commit()
    session.close() 