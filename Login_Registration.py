'''
Registration()
This is the class that controls the user's registration and login information. 

Registration() attributes:
This class has no attributes of its's own. This class will extend and use all 
attributes from the User Class.

Registration() methods: 
register(): Takes in user information and allows them to create a new account.
login(): Allows user to login with a username and password. 
'''
class Registration:
    '''
    Function to let new users register
    Input: Currently users only need to enter their first name, last name, chosen username
    and password.
    Output: A new user will be created with the information entered. 
    In next development iteration, users will need to be given a unique temporary username and
    password to login and set up their own account. 
    '''
    def register():
        users = {} #To store all username and password combos
        try: #Currently storing user info in a txt file, can figure out details later
            with open("users.txt", "r") as file:
                for line in file:
                    user, passw = line.strip().split(":")
                    users[user] = passw
        except FileNotFoundError:
            pass
        '''
        Generic user and password. This will be used when backend is implemented.
        Each new user will be given a unique temporary login. 
        This will allow them access to their company's login page
        to register.
        '''
        unique_user = "user2"
        unique_pass = "pass2"
        users[unique_user] = unique_pass #Store the given user and pass

        if unique_user in users and users[unique_user] == unique_pass:
            print("Please set up your user details: ")
            #Get general info from user
            first_name = input( "Enter First Name: ")
            last_name = input( "Enter Last Name: ")
            username = input( "Enter Username: ")
            password = input("Enter a Password: ")
            #User will be assigned a position rank from the unique login 
            #they were given to login with
    
        #Check if username already exists
        if username in users:
            print("Username already exists. Please choose another username.")
        else:
            users[username] = password #Store username and password
            print("Registration successful! Please login")
            Registration.login()
    
    '''
    Function to let users login to their account.
    Input: User's username and password
    Output: If login is successful, the user will be 
    taken to the homepage of the software.
    '''
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
'''
Called upon start up.
Input: User's are allow to select either login or register, valid inputs
include 1 or 2 via the keyboard.
Output: Users will be directed to the page of their choosing,
either login page or registration page.
'''
def main():
    choice = input("To Register, Press 1 \nTo Login, Press 2\n")
    if choice == "1":
        Registration.register()
    elif choice == "2":
        Registration.login()
    else:
        print("Invalid selection")

    
if __name__ == "__main__":
    main()
