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

class Project:
    project_name = ""
    project_id = -1
    deadline = ""
    priority = 0
    owner = ""
    tasks = list()
    
    """
    __init__(...): Paramaterized constructor for the Project class. When called, it initializes the 
                   of the Project() object and stores the provided variables correspondingly.
    
    parameters:
        all the attributes described at the top of this class (see comment above)

    """
    def __init__(self, project_name, project_id, deadline, priority, owner, tasks):
        self.project_name = project_name
        self.project_id = project_id
        self.deadline = deadline
        self.priority = priority
        self.owner = owner
        self.tasks = tasks
    
    """
    print_tasks(project): Prints the names of the tasks assigned to this project.

    parameters:
        project: a Project object that system will print the tasks of [PROJECT()] 
    """
    def print_tasks(project):
        if bool(project.tasks):
            count = 1
            for i in project.tasks:
                print("     Task " + str(count) + ": " + i.task_name)
                count = count + 1
        else:
            print("No Tasks yet.")
    
    """
    print_project_details(task): Prints all of the project attributes in clear format.

    parameters:
        proj: a Project object that system will print details of [PROJECTS()] 
    """
    def print_project_details(proj):
        print("Project Name: " + proj.project_name)
        print("Project ID: " + str(proj.project_id))
        print("Project Deadline: " + proj.deadline)
        print("Project Priority: " + proj.priority)
        print("Project Manager: " + proj.owner)
        print("All assigned tasks: ")
        Project.print_tasks(proj)

    """
    create_tasks(self): Prompts user input for a new task added to the current instance of the Project.

    parameters:
        self: the current instance of the Project object in this class
    """
    def create_task(self):
        print("Please enter task details: ")

        task_name = input("Enter the name of the task: ")
        assigned_project = input("Provide the ID of the Project this task is assigned to (numeric): ")
        priority = input("Priority? (Enter High, Medium, or Low): ")
        capability_level = input("Capability Level (integer between 1 and 5): ")
        deadline = input("Task Deadline (DD-MM-YYYY): ")
        assigned_to = ""
        project_portion = input("Enter the portion of the project (e.g. 0.25 is 25%): ")

        new_task = Task(task_name, assigned_project, priority, capability_level, deadline, assigned_to, project_portion)
        self.tasks.append(new_task)

