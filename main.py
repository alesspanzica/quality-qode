import subprocess
from project_manager import ProjectManager

from user import User
from user_profile import Profile
from registration import Registration


def main():
    while(1):
        print()
        print("Welcome to Task Management, a web application that helps you manage your projects and tasks!")

        subprocess.run(["python", "registration.py"])
        #global_username = Registration.reg_main()
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
