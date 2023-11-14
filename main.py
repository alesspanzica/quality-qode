import subprocess
from sqlalchemy.orm import Session
from database import createSession

from model import Task as TaskModel
from model import Project as ProjectModel
from sqlalchemy import delete

def main():
    """     
    session = createSession()
    project = session.query(ProjModel).filter(ProjModel.project_id == 3000).first()
    project.owner = "Emily Johnson"
    session.commit()
    session.close() 
    """

    while(1):
        print()
        print("Welcome to Task Management, a web application that helps you manage your projects and tasks!")

        subprocess.run(["python", "registration.py"])
        print()

        print("Now lets select a page you want to view!")
        print(" Home page - Enter 1\n Project Manager Page - Enter 2\n User Profile Page - Enter 3")
        
        user_input = input("Enter what page, otherwise 0 to terminate: ")
        print()
        if user_input.isdigit():
            num_in = int(user_input)
            if num_in == 0:
                print("Program terminated. Goodbye!")
                break
            elif num_in == 1:
                subprocess.run(["python", "home.py"])
            elif num_in == 2:
                subprocess.run(["python", "project_manager.py"])
            elif num_in == 3:
                subprocess.run(["python", "user_profile.py"])
            else:
                print("Not proper input. Try again!")
        else:
            print("Not proper input. Try again!")

    return 0

if __name__ == "__main__":
    main()
