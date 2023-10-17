#Class to store user info
#class Users:
#    def __init__(self, first_name, last_name, username, password):
#        self.first_name = first_name
#        self.last_name = last_name
#        self.username = username
#        self.password = password

    #Function to let new users register
def register():
    users = {} #To store all username and password combos
    try: #Currently storing user info in a txt file, can figure out details later
        with open("users.txt", "r") as file:
            for line in file:
                user, passw = line.strip().split(":")
                users[user] = passw
    except FileNotFoundError:
        pass

    #Generic user and password for now
    unique_user = "user2"
    unique_pass = "pass2"
    users[unique_user] = unique_pass #Store the given user and pass

    if unique_user in users and users[unique_user] == unique_pass:
        print("Please set up your user details: ")
        #Get general info from user
        #Left out position stuff for now, unsure how we wanted to do that
        first_name = input( "Enter First Name: ")
        last_name = input( "Enter Last Name: ")
        username = input( "Enter Username: ")
        password = input("Enter a Password: ")
    
    #Check if username already exists
    if username in users:
        print("Username already exists. Please choose another username.")
    else:
        users[username] = password #Store username and password
        print("Registration successful! Please login")
        login()
        
def login():
    users = {} #To store all username and password combos
    try: 
        with open("users.txt", "r") as file:
            for line in file:
                user, passw = line.strip().split(":")
                users[user] = passw
    except FileNotFoundError:
        print("No users Registered")
        return 
        
    username = input( "Enter Username: ")
    password = input("Enter a Password: ")
    if username in users and users[username] == password:
        print("Login Successful.")
    else:
        print("Login Failed. Check username and password.")

#Login or Register Selection
def main():
    choice = input("To Register, Press 1 \nTo Login, Press 2\n")
    if choice == "1":
        register()
    elif choice == "2":
        login()
    else:
        print("Invalid selection")

    
if __name__ == "__main__":
    main()