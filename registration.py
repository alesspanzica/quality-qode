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
from user import User 
from sqlalchemy.orm import Session
from database import createSession
from user_model import User as UserModel
from getpass import getpass

class Registration:
    '''
    Function to let users login to their account.
    Input: User's username and password
    Output: If login is successful, the user will be 
    taken to the homepage of the software.
    '''
    def login():
        username = input("Enter Username: ")
        password = getpass("Enter a Password: ") #Blurred password

        #Checks if username and password entered match. 
        session = createSession()
        user = session.query(UserModel).filter(UserModel.username == username,
                                          UserModel.password == password).first()
        session.close()
        if user:
            print("Login Successful.")
        else:
            print("Login Failed. Check username and password.")
            Registration.login() #Recalls login() to have user enter their details again

    '''
    Function to let new users register
    Input: Currently users only need to enter their first name, last name, chosen username
    and password.
    Output: A new user will be created with the information entered. 
    In next development iteration, users will need to be given a unique temporary username and
    password to login and set up their own account. 
    '''
    def register():
        print("Please set up your user details: ")
        #Get general info from user
        name = input( "Enter Name: ")
        username = input( "Enter Username: ")
        password = input("Enter a Password: ")#Not blurred so user can verify password
        phone_number = input("Enter your phone number: ")
        address = input("Enter your address: ")
        email = input("Enter your email: ")

        #Checks if this username is already in use
        session = createSession()
        exsiting_user = session.query(UserModel).filter(UserModel.username == username).first()
        if exsiting_user:
            print("Username already exists. Please choose another.")
            session.close()
            username = input( "Enter Username: ")
        #Creates a new User object and inserts it into the database table.
        else:
            new_user = UserModel(
                username = username,
                password = password,
                name=name,
                phone_number=phone_number,
                address=address,
                email=email,
                position="position",
                manager="manager"
            )
            session.add(new_user) #Add new user info to table
            session.commit()
            session.close()

        print("Registration successful! Please log in.")
        Registration.login()


#Login or Register Selection
'''
Called upon start up.
Input: User's are allow to select either login or register, valid inputs
include 1 or 2 via the keyboard.
Output: Users will be directed to the page of their choosing,
either login page or registration page.
'''
def reg_main():
    choice = input("To Register, Press 1 \nTo Login, Press 2\n")
    if choice == "1":
        Registration.register()
    elif choice == "2":
        Registration.login()
    else:
        print("Invalid selection")

    
if __name__ == "__main__":
    reg_main()
