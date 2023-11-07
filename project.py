"""
Project()
This is the class that represents the Project object. This is the parent class for the task object since an instance of the 
Project object will include Tasks associated. Note all fields are required for the user to input when a project is created.

    Project() attributes:
        project_name: name of the project [STRING]
        project_ID: associated project ID of the project [INTEGER]
        deadline: the project deadline in DD-MM-YYYY format [STRING]
        priority: priority level - High, Medium, or Low [STRING]
        owner: the username of the manager/owner of the project [STRING]
        tasks: the username of the person this task is assigned to [STRING]
    
    Project() methods:
        __init__(self, project_name, project_id, deadline, priority, owner, tasks): parameterized constructor
        print_tasks(project): prints all the task names within this project
        print_project_details(proj): prints all project attributes to the user clearly when called
        create_task(self): creates a new instance of the Task object and appends it to this instance of the Project object's list of tasks attribute
"""
from task import Task
from sqlalchemy.orm import Session
from database import createSession

from model import Task as TaskModel
from model import Project as ProjModel

class Project:
    project_name = ""
    project_id = -1
    deadline = ""
    priority = 0
    owner = ""
    num_of_tasks = 0
    
    """
    __init__(...): Paramaterized constructor for the Project class. When called, it initializes the 
                   of the Project() object and stores the provided variables correspondingly.
    
    parameters:
        all the attributes described at the top of this class (see comment above)

    """
    def __init__(self, project_name, project_id, deadline, priority, owner, num_of_tasks):
        self.project_name = project_name
        self.project_id = project_id
        self.deadline = deadline
        self.priority = priority
        self.owner = owner
        self.num_of_tasks = num_of_tasks
    
    """
    print_tasks(project_id): Prints the names of the tasks assigned to this project.

    parameters:
        project: a Project object that system will print the tasks of [PROJECT()] 
    """
    def print_tasks(project_id):
        session = createSession()
        tasks = session.query(TaskModel.task_name).filter(TaskModel.assigned_project == project_id).all()
        
        if tasks:
            print(tasks)
            '''#
            for row in tasks:
                print("\n     Task " + str(row.task_num_in_project) + ": " + row.task_name)
            '''
        else:
            print("\nNo Tasks yet.")

        session.close()
    
    """
    print_project_details(task): Prints all of the project attributes in clear format.

    parameters:
        proj: a Project object that system will print details of [PROJECTS()] 
    """
    def print_project_details(proj):
        print("\nProject Name: " + proj.project_name)
        print("Project ID: " + str(proj.project_id))
        print("Project Deadline: " + proj.deadline)
        print("Project Priority: " + proj.priority)
        print("Project Manager: " + proj.owner)
        print("All " + str(proj.num_of_tasks) + " assigned tasks: ")
        Project.print_tasks(proj.project_id)

    """
    create_tasks(self): Prompts user input for a new task added to the current instance of the Project.

    parameters:
        self: the current instance of the Project object in this class
    """
    def create_task(self):
        print("\nPlease enter task details: ")

        task_name = input(" Enter the name of the task: ")
        assigned_project = input(" Provide the ID of the Project this task is assigned to (numeric): ")
        priority = input(" Priority? (Enter High, Medium, or Low): ")
        capability_level = input(" Capability Level (integer between 1 and 5): ")
        deadline = input(" Task Deadline (DD-MM-YYYY): ")
        project_portion = input(" Enter the portion of the project (e.g. 0.25 is 25%): ")


        session = createSession()
        exisiting_task = session.query(TaskModel).filter(
            TaskModel.task_name == task_name & TaskModel.assigned_project == assigned_project).first()

        if exisiting_task:
            print("Task already exists in project " + str(assigned_project) + ". Please use another name for that project.")
            session.close()
            task_name = input( "Enter the name of the task: ")
        #Creates a new Task object and inserts it into the database table.
        else:
            task_num = session.query(ProjModel.num_of_tasks).filter(ProjModel.project_id == assigned_project)
            task_num = task_num + 1

            new_task = TaskModel(
                task_name = task_name,
                assigned_project = assigned_project,
                priority = priority,
                capability_level = capability_level,
                deadline = deadline,
                assigned_to = "",
                task_num_in_project = task_num,
                project_portion = project_portion
            )
            session.add(new_task) #Add new task info to table
            session.commit()
            session.close()

