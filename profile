"""
Task()
This is the class that represents the Task object. Note all fields are
required for the user to input when a task is created except for the
'assigned_to' field, which can be updated at any time (this is more
related to the backend design).

Profile()
This is the class that represents the Profile object. 

    Profile() attributes:

    Profile() methods:


    Task() attributes:
        task_name: name of the task [STRING]
        assigned_project: project ID this task is part of [INTEGER]
        priority: priority level - High, Medium, or Low [STRING]
        capability_level:
        deadline:
        assigned_to:
        project_portion:

    Task() methods:
        __init__(self, task_name, assigned_project, priority, capability_level, deadline, assigned_to, project_portion): parameterized constructor
        print_task_details(task): prints all task attributes to the user clearly when called
        assign_task(self, assigned_to): assigns the task to a particular user at any time (for backend purposes)

"""

'''class User():
    def __init__(self):
    self.username = ""
    self.name = ""
    self.phone_number = ""
    self.address = ""
    self.email = ""
    self.position = ""
    self.manager = ""
    self.bio = ""
    self.picture  = ""
'''
from user import User

class Profile:
    def Load(username):
        users = []
        try: 
            with open("users.txt", "r") as file:
                for line in file:
                    username, passw, name, phonenumber, address, email, position, manager, bio = line.strip().split(":")
                    users[username] = passw
        except: None


def CLI(dict):
    temp = list(dict.keys())
    inp = input("Actions: View : " + str(temp) + "\n")
    def ProfilePage(profile, dict):
        inp2 = input("Actions: View or Edit " + str(profile) + ", or type 'Back' to return to Profiles List\n")
        if inp2 == "Back":
            CLI(dict)
        elif inp2 ==  "View":
            for property, value in vars(profile).items():
                print(property, ":" , value)
            ProfilePage(profile, dict)
        elif inp2 == "Edit":
            vardict = vars(profile).items()
            for property, value in vardict:
                print(property, ":" , value)
            inp3 = input("What field would you like to change?\n")
            
            if inp3 is property in vardict: #broken
                inp4 = input("Enter new value:\n")
                property.value = inp4
            else:
                print("Unrecognized Input.")
                
            ProfilePage(profile, dict)
        else:
            print("Unrecognized Input.")
    
    if inp in temp:
        ProfilePage(dict[inp], dict)
    else:
        print("Unrecognized Input.")
        CLI(dict)
    

def main():
    person = User()
    person.username = "a1"
    person.name = "Jim"
    person.phonenumber =  "33333"
    person.address = "3 Teirgarten Avenue"
    person.email = "s"
    person.position = "d"
    #person.manager
    person.bio = ""
    allprofiles = {str(person):person}
    CLI(allprofiles)
    allprofiles.keys()
    view = input("username, passw, name, phonenumber, address, email, position, manager, bio")


if __name__ == "__main__":
    main()
