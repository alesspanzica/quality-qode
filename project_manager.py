"""
ProjectManager()
This is the class that represents the ProjectManager object class. This is the parent class for the Project object since an instance of the 
ProjectManager object will include Profile associated. Note all fields are required for the user to input when a project is created.

    Project() attributes:
        projects: represents list of Project objects [list(PROJECTS())]
    
    Project() methods:
        __init__(self): empty constructor
        create_project(self): creates a new instance of the Project object
        print_projects(self):
        find_project(project_id): 
        add_task(project): 
"""
import sys
from project import Project
from task import Task

from sqlalchemy.orm import Session
from database import createSession

from model import Project as ProjectModel
from model import Task as TaskModel
from model import User as UserModel

class ProjectManager:
    """
    create_project(self): creates a new Project object provided by the user
                            and appends it to the projects attribute within this
                            instance of the Project Manager
    parameters:
        self: the instance of ProjectManager within this class that the project gets appended to
    """
    def create_project():
        print("Please enter Project details: ")

        project_name = input("Enter the name of the project: ")
        project_id = input("Enter the project's ID: ")
        deadline = input("Project Deadline (DD-MM-YYYY): ")
        priority = input("Priority: ")
        owner = input("Enter the username of the project's manager: ")
        tasks = list()

        self.append(Project(project_name, project_id, deadline, priority, owner, tasks))
    
    """
    print_projects(self): Prints the names of the projects in the project list.

    parameters:
        self: the instance of ProjectManager within this class
    """
    def print_projects():
        username = input('Please enter your username to view all team projects: ')
        
        session = createSession()
        manager = session.query(UserModel.manager).filter(UserModel.username == username)
        your_projects = session.query(ProjectModel.project_name, ProjectModel.project_id).filter(ProjectModel.owner == manager).first()
    
        if your_projects is None:
            session.close()
            return input("No current projects. To create a project, enter C: ")
        else:
            '''
            for i in your_projects:
                print(i)
            '''
            print(your_projects)
            session.close()
            return input("Enter the ID of the project you want to view and add tasks to. To create a project, enter C: ")

    """
    find_project(project_id): this returns the project object with a specific
                                project ID

    parameters:
        project_id: the ID of the project that the method searches for [INTEGER]
    """
    def find_project(project_id):
        session = createSession()
        project = session.query(ProjectModel).where(project_id = project_id)
        session.close()
        return project


    
    """
    add_task(project): adds a task to a specific project in the project list

    parameters:
        project: the project that the specified task is being added to
    """
    def add_task(project):
        project.create_task()
        print("Task created and added to Project " + str(project.project_id) + ".")

"""
This is the main method that runs the Project Manager Page of the web app. 
"""
def project_main():
    print("*** ENTER 0 AT ANY TIME TO RETURN TO HOMEPAGE ***")
    print("Welcome to the Projects page! Here you can view or create projects!")
    user_input = ''

    '''
    project_list = ProjectManager()
    project_list.projects.append(Project("Front End Prototype", 2000, "20-10-2023", "Medium", "alessiapanzica", [Task("Make Documentation PDF", 2000, "Low", 2, "01-09-2023", "jasperlim", 0.05), Task("User Registration Classes", 2000, "High", 5, "01-10-2023", "abbeycameron", 0.25)]))
    project_list.projects.append(Project("Front End User Testing", 3000, "2-11-2023", "Medium", "alessiapanzica", [Task("Make Documentation PDF", 3000, "Medium", 2, "15-09-2023", "jasperlim", 0.25), Task("Prepare User I/O File", 3000, "High", 2, "15-10-2023", "abbeycameron", 0.45), Task("Report Presentation Slide Deck", 3000, "Medium", 2, "01-10-2023", "abbeycameron", 0.10)]))
    '''
    print()

    while(1):
        print("Below is the list of current projects.")
        user_input = ProjectManager.print_projects()

        if user_input == 'C':
            project_list.create_project()
            print("Project Created!")
            print()

        elif user_input.isdigit():
            if user_input == '0':
                print("Exiting Projects Page, returning to Home Page!")
                break
            
            print()
            project = ProjectManager.find_project(user_input) 

            if project == None:
                print("Sorry, project doesn't exist. Try again.")
                continue
            
            Project.print_project_details(project)

            print()
            while(1):
                user_input = input("Enter the number of the task you want to view, enter A to add a task to this project, otherwise enter 0: ")
                if user_input == 'A':
                    Project.create_task(project.project_id)
                    print("Task created and added to Project " + str(project.project_id) + ".")
                    print()
                    continue
                elif user_input.isdigit():
                    num = int(user_input)
                    if num == 0:
                        print("Exiting Projects Page, returning to homepage.")
                        return 
                    
                    else:
                        session = createSession()
                        task = session.query(TaskModel).filter(TaskModel.task_num_in_project == num)
                        print(task)
                        # task.print_task_details()
                        session.close()
                        break
                else:
                    current_proj.tasks[int(user_input)-1].print_task_details

        else:
            print()
            print("Please enter a proper input. Try again.")
    

