import sqlalchemy
import pytest
import unittest
import subprocess

from project_manager import ProjectManager
from model import ProjectModel
from model import TaskModel

from sqlalchemy.orm import Session
from database import createSession
from sqlalchemy.exc import IntegrityError

class CreateProjectsTasks:
    def setup_class(self):
        self.session = createSession()
        self.valid_project = ProjectModel(
            project_name = "Test Project",
            project_id = 1234,
            deadline = "01-01-01",
            priority = "Low",
            owner = "Samuel Patel",
            num_of_tasks = 0
        )
        self.valid_task = TaskModel(
            task_name = "Test Task",
            assigned_project = 1234,
            priority = "Low",
            capability_level = 1,
            deadline = "01-01-01",
            task_num_in_project = 1,
            project_portion = 0.0
        )

    def test_db_project_valid(self):   
        self.session.add(self.valid_project)
        self.session.commit()
        test_proj_query = self.session.query(ProjectModel).filter_by(project_id=1234).first()
        assert test_proj_query.project_name == "Test Project"
        assert test_proj_query.project_id != 1235
        assert test_proj_query.deadline == "01-01-01"
        assert test_proj_query.priority == "Low"
        assert test_proj_query.owner == "Samuel Patel"
        assert test_proj_query.num_of_tasks == 0
    
    def test_db_task_valid(self):   
        self.session.add(self.valid_task)
        self.session.commit()
        test_task_query = self.session.query(TaskModel).filter_by(task_num_in_project=1, assigned_project=1234).first()
        assert test_task_query.project_name == "Test Task"
        assert test_task_query.assigned_project != 1235
        assert test_task_query.priority == "Low"
        assert test_task_query.capability_level == 1
        assert test_task_query.deadline == "01-01-01"
        assert test_task_query.num_of_tasks != 0
        assert test_task_query.project_portion == 0.0

    @pytest.mark.xfail(raises=IntegrityError)
    def test_db_project_missing_field(self):
        testing = ProjectModel(
            project_name = "Test Project 1",
            project_id = 2345,
            deadline = "10-10-10",
            priority = "Low",
            num_of_tasks = 0
        )
        self.session.add(testing)
        try:
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
    
    @pytest.mark.xfail(raises=IntegrityError)
    def test_db_task_missing_field(self):
        testing = TaskModel(
            project_name = "Test Project 1",
            project_id = 2345,
            deadline = "10-10-10",
            priority = "Low",
            num_of_tasks = 0
        )
        self.session.add(testing)
        try:
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
    
   # def test_func_project_valid(self):


    def teardown_class(self):
        self.session.rollback()
        self.session.close()