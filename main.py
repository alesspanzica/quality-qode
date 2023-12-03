import subprocess


def main():
    print()
    print("Welcome to Task Management, a web application that helps you manage your projects and tasks!")

    reg = subprocess.run(["python", "registration.py"])
    if reg.returncode == 1:
        print("Program terminated. Goodbye!")
        exit(1)

    while(1):
        print()
        print("Now lets select a page you want to view!")
        print(" Home page - Enter 1\n Project Manager Page - Enter 2\n User Profile Page - Enter 3")
        
        user_input = input("Enter what page, otherwise 0 to terminate: ")
        print()
        if user_input.isdigit():
            num_in = int(user_input)
            if num_in == 0:
                print("Program terminated. Goodbye!")
                exit(1)
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

    exit(0)

if __name__ == "__main__":
    main()
