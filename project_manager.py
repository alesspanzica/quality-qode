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
from project import Project
from task import Task

from sqlalchemy.orm import Session
from database import createSession

from model import Project as ProjectModel
from model import Task as TaskModel
from model import User as UserModel

import warnings
from sqlalchemy import exc as sa_exc

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
        if project_name == "":
            project_name = input("You must enter a name. Try again: ")
        project_id = input("Enter the project's ID: ")
        deadline = input("Project Deadline (DD-MM-YYYY): ")
        priority = input("Priority: ")
        owner = input("Enter the name of the project's manager: ")
        session = createSession()
        exisiting_proj = session.query(ProjectModel).filter(ProjectModel.project_id == project_id).first()

        if exisiting_proj:
            print("Project already exists. Try again.")
            session.close()
        #Creates a new User object and inserts it into the database table.
        else:
            new_project = ProjectModel(
                project_name = project_name,
                project_id = project_id,
                deadline = deadline,
                priority = priority,
                owner = owner,
                num_of_tasks = 0
            )
            session.add(new_project) #Add new user info to table
            session.commit()
            session.close()
            print("Project created successfully.")

    """
    print_projects(self): Prints the names of the projects in the project list.

    parameters:
        self: the instance of ProjectManager within this class
    """
    def print_projects():
        username = input('Please enter your username to view all team projects: ')
        
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=sa_exc.SAWarning)

            session = createSession()
            manager = session.query(UserModel.manager).filter(UserModel.username == username)
            your_projects = session.query(ProjectModel).filter(ProjectModel.owner == manager).all()
        
            print("Below is the list of your manager's current projects.")
            if your_projects:
                print()
                for i in your_projects:
                    print("  Project " + str(i.project_id) + ": " + i.project_name)
                print()
                session.close()
                return input("Enter the ID of the project you want to view and add tasks to. To create a project, enter C: ")
            else:
                session.close()
                return input("No current projects. To create a project, enter C: ")

    """
    print_project_details(project): Prints all of the project attributes in clear format.

    parameters:
        self: current Project object that system will print details of [PROJECTS()] 
    """
    def print_project_details(project):
        print("\nProject Name: " + project.project_name)
        print("Project ID: " + str(project.project_id))
        print("Project Deadline: " + project.deadline)
        print("Project Priority: " + project.priority)
        print("Project Manager: " + project.owner)
        print("All " + str(project.num_of_tasks) + " assigned tasks: ")
        Project.print_tasks(project.project_id)
    
    """
    print_task_details(task): Prints all of the task attributes in clear format.

    parameters:
        task: a task object that system will print details of [TASK()] 
    """
    def print_task_details(task):
        print("\nTask " + str(task.task_num_in_project) + ": " + task.task_name)
        print("  Assigned Project: " + task.assigned_project)
        print("  Priority: " + task.priority)
        print("  Capability Level: " + str(task.capability_level))
        print("  Project Deadline: " + task.deadline)
        percentage = float(task.project_portion) * 100
        print("  Portion of Project: " + str(percentage) + "%")
        if task.assigned_to == "":
            print("  Task is currently UNASSIGNED.")
            user_input = input("Enter A to assigned this task to a user, or enter 0 to continue: ")
            if user_input == 'A':
                ProjectManager.assign_task_to(task.task_num_in_project, task.assigned_project)
            else:
                return
        else:
            print("  Task Assigned To: " + task.assigned_to)

    def assign_task_to(task_num, project_id):
        assigned = input(" Who would you like to assign this task to? Enter the username: ")
        
        session = createSession()
        task = session.query(TaskModel).filter(TaskModel.assigned_project == project_id, TaskModel.task_num_in_project == task_num).first()
        task.assigned_to = assigned
        session.commit()
        session.close()

        print("Task successfully assigned to " + assigned + ".")


    """
    find_project(project_id): this returns the project object with a specific
                                project ID

    parameters:
        project_id: the ID of the project that the method searches for [INTEGER]
    """
    def find_project(project_id):
        session = createSession()
        project = session.query(ProjectModel).filter(ProjectModel.project_id == project_id).first()
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



# This is the main method that runs the Project Manager Page of the web app. 
def project_main():

    print("*** ENTER 0 AT ANY TIME TO RETURN TO HOMEPAGE ***")
    print("Welcome to the Projects page! Here you can view or create projects!")
    user_input = ''

    print()

    while(1):
        user_input = ProjectManager.print_projects()

        if user_input == 'C':
            ProjectManager.create_project()
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
            
            ProjectManager.print_project_details(project)

            print()
            while(1):
                user_input = input("Enter the number of the task you want to view, enter A to add a task to this project, otherwise enter 0: ")
                if user_input == 'A':
                    Project.create_task(project.project_id)
                    print("Task created and added to Project " + str(project.project_id) + ".")
                    print()
                    break
                elif user_input.isdigit():
                    num = int(user_input)
                    if num == 0:
                        print("Exiting Projects Page, returning to homepage.")
                        return 
                    
                    else:
                        session = createSession()
                        task = session.query(TaskModel).filter(TaskModel.task_num_in_project == num, TaskModel.assigned_project == project.project_id).first()
                        print()
                        ProjectManager.print_task_details(task)
                        session.close()
                        break
                else:
                    print("\nPlease enter a proper input. Try again.")

if __name__ == "__main__":
    project_main()
