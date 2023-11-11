"""
Task()
This is the class that represents the Task object. Note all fields are
required for the user to input when a task is created except for the
'assigned_to' field, which can be updated at any time (this is more
related to the backend design).

    Task() attributes:
        task_name: name of the task [STRING]
        assigned_project: project ID this task is part of [INTEGER]
        priority: priority level - High, Medium, or Low [STRING]
        capability_level: clearence level the assigned user should have in order to be assigned this task [INTEGER]
        deadline: the task deadline in DD-MM-YYYY format [STRING]
        assigned_to: the username of the person this task is assigned to [STRING]
        task_num_in_project = 
        project_portion: how much of the project this task contributes to (e.g. 0.25 is 25% of project) [FLOAT]

    Task() methods:
        __init__(self, task_name, assigned_project, priority, capability_level, deadline, assigned_to, project_portion): parameterized constructor
        print_task_details(task): prints all task attributes to the user clearly when called
        assign_task(self, assigned_to): assigns the task to a particular user at any time (for backend purposes)

"""
class Task:
    task_name = ""
    assigned_project = -1
    priority = ""
    capability_level = 0
    deadline = ""
    assigned_to = ""
    task_num_in_project = 0
    project_portion = 0.0

    """
    __init__(...): Paramaterized constructor for the Task class. When called, it initializes the 
                   of the Task() object and stores the provided variables correspondingly.
    
    parameters:
        all the attributes described at the top of this class (see comment above)

    """
    def __init__(self, task_name, assigned_project, priority, capability_level, deadline, task_num_in_project, project_portion):
        self.task_name = task_name
        self.assigned_project = assigned_project
        self.priority = priority
        self.capability_level = capability_level
        self.deadline = deadline
        self.assigned_to = ""
        self.task_num_in_project = task_num_in_project
        self.project_portion = project_portion

    """
    assign_task(self, assigned_to): will update the assigned_to attribute and
                                    assign the proper username of that user

    parameters:
        self: the instance of this specific object [TASK()]
        assigned_to: username of the user this task gets assigned to [STRING]
    """
    def assign_task(self, assigned_to):
        self.assigned_to = assigned_to
