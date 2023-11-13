import sqlalchemy
import pytest
from unittest import TestCase
import subprocess

from project_manager import ProjectManager
from model import ProjectModel
from model import TaskModel

from sqlalchemy.orm import Session
from database import createSession
from sqlalchemy.exc import IntegrityError

class CreateProjects:
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

    def test_project_valid(self):   
        self.session.add(self.valid_author)
        self.session.commit()
        test_proj_query = self.session.query(ProjectModel).filter_by(project_id=1234).first()
        assert test_proj_query.project_name == "Test Project"
        assert test_proj_query.project_id != 1235
        assert test_proj_query.deadline == "01-01-01"
        assert test_proj_query.priority == "Low"
        assert test_proj_query.owner == "Samuel Patel"
        assert test_proj_query.num_of_tasks == 0

    @pytest.mark.xfail(raises=IntegrityError)
    def test_project_missing_field(self):
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

    def teardown_class(self):
        self.session.rollback()
        self.session.close()