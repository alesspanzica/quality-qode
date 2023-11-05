"""
ProjectManager()
This is the class that represents the ProjectManager object class. This is the parent class for the Project object since an instance of the 
ProjectManager object will include Profile associated. Note all fields are required for the user to input when a project is created.

    Project() attributes:
        projects: represents list of Project objects [list(PROJECTS())]
    
    Project() methods:
        __init__(self): empty constructor
        create_project(self): creates a new instance of the Project object
        print_project_details(self):
        index_of_project(project_id): 
        add_task(project): 
"""
import sys
from project import Project
from task import Task

class ProjectManager:
    """
    __init__(): Empty constructor for the ProjectManager. When called, it initializes the 
                of the ProjectManager() object and initializes the attribute to an empty list.
    
    parameters:
        self: the instance of ProjectManager within this class that gets initialized to an empty list
    """
    def __init__(self):
        self.projects = list()

    """
    create_project(self): creates a new Project object provided by the user
                            and appends it to the projects attribute within this
                            instance of the Project Manager
    parameters:
        self: the instance of ProjectManager within this class that the project gets appended to
    """
    def create_project(self):
        print("Please enter Project details: ")

        project_name = input("Enter the name of the project: ")
        project_id = input("Enter the project's ID: ")
        deadline = input("Project Deadline (DD-MM-YYYY): ")
        priority = input("Priority: ")
        owner = input("Enter the username of the project's manager: ")
        tasks = list()

        self.projects.append(Project(project_name, project_id, deadline, priority, owner, tasks))
    
    """
    print_projects(self): Prints the names of the projects in the project list.

    parameters:
        self: the instance of ProjectManager within this class
    """
    def print_projects(self):
        for i in self.projects:
            print("Project " + str(i.project_id) + ": " + i.project_name)

    """
    index_of_project(project_id): this returns the index of a Project object with a specific
                                    project ID

    parameters:
        project_id: the ID of the project that the method searches for [INTEGER]
    """
    def index_of_project(project_id):
        return next((i for i, obj in enumerate(project_list.projects) if obj.project_id == project_id), -1)
    
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
if __name__ == "__main__":
    print("*** ENTER 0 AT ANY TIME TO RETURN TO HOMEPAGE ***")
    print("Welcome to the Projects page! Here you can view or create projects!")

    user_input = ''
    project_list = ProjectManager()
    project_list.projects.append(Project("Front End Prototype", 2000, "20-10-2023", "Medium", "alessiapanzica", [Task("Make Documentation PDF", 2000, "Low", 2, "01-09-2023", "jasperlim", 0.05), Task("User Registration Classes", 2000, "High", 5, "01-10-2023", "abbeycameron", 0.25)]))
    project_list.projects.append(Project("Front End User Testing", 3000, "2-11-2023", "Medium", "alessiapanzica", [Task("Make Documentation PDF", 3000, "Medium", 2, "15-09-2023", "jasperlim", 0.25), Task("Prepare User I/O File", 3000, "High", 2, "15-10-2023", "abbeycameron", 0.45), Task("Report Presentation Slide Deck", 3000, "Medium", 2, "01-10-2023", "abbeycameron", 0.10)]))

    while(1):
        print()
        print("Below is the list of current projects.")
        ProjectManager.print_projects(project_list)
        user_input = input("Enter the ID of the project you want to view and add tasks to. To create a project, enter C: ")

        if user_input == 'C':
            project_list.create_project()
            print("Project Created!")
            print()

        elif user_input.isdigit():
            if user_input == '0':
                print("Exiting Projects Page, returning to Home Page!")
                break
            
            print()
            index = ProjectManager.index_of_project(int(user_input)) 
            if index == -1:
                print("Sorry, project doesn't exist. Try again.")
                continue
            
            current_proj = project_list.projects[index]
            Project.print_project_details(current_proj)

            print()
            user_input = input("Enter the number of a task you want to view, enter A to add a task to this project, otherwise enter 0: ")
            if user_input == 'A':
                ProjectManager.add_task(current_proj)
            elif user_input.isdigit():
                if int(user_input == 0):
                    print("Exiting Projects Page, returning to homepage.")
                    break
                else:
                    current_proj.tasks[int(user_input)-1].print_task_details()

        else:
            print()
            print("Please enter a proper input. Try again.")
    

