"""
Profile()
This is the class that represents the Profile object. 

    Profile() attributes:
    -

    Profile() methods:

        all_page(): Prepares CLI to interact with profiles, organizing all known profiles

        profile_page(profile): Enables user to view and edit profile information in CLI

"""

from user import User 
from sqlalchemy.orm import Session
from sqlalchemy import select, update
from database import createSession
from model import User as UserModel
from getpass import getpass


class Profile:
    user_profiles = None

    def profile_page(profile):
        
        inp2 = input("Actions: View or Edit " + str(profile) + ", or type 'Back' to return to Profiles List\n") #CLI input
        if inp2 == "Back":
            Profile.all_page()

        elif inp2 ==  "View": #prints all User variables and their values
            session = createSession()
            x = session.query(UserModel).filter(UserModel.username == profile)
            for row in x :
                print(row.username, row.name, row.phone_number, row.address, row.email, row.position, row.manager)
            session.close()    
            Profile.profile_page(profile)

        elif inp2 == "Edit":
            session = createSession()
            x = session.query(UserModel).filter(UserModel.username == profile)
            for row in x :
                print(row.username, row.name, row.phone_number, row.address, row.email, row.position, row.manager) 
            inp3 = input("What field would you like to change?\n")
            q = session.query(UserModel).filter(UserModel == inp3)
            if session.query(q.exists()):
                inp4 = input("Enter new value:\n")
                session.query(UserModel).filter(UserModel.username == profile).update({inp3: inp4})
                session.commit()
                session.close()
                if inp3 == "username":
                    Profile.profile_page(inp4)
            else:
                print("Unrecognized Input.")
            Profile.profile_page(profile) #return to CLI for 
        
        elif (inp2 == "Exit") or (inp2 == "exit"):
            return
        
        else:
            print("Unrecognized Input.")
            Profile.profile_page(profile)

    def all_page():
        session = createSession()
        temp = session.query(UserModel.username) #get User class variables in list
        temp2 = []
        for x in temp: 
            temp2.append(x[0])
        inp = input("Select a Profile:" + str(temp2) + "\n")
        if inp in temp2: #if valid profile selected...
            Profile.profile_page(inp)
            session.close()
        elif inp == "Exit" or inp == "exit":
            return
        else:
            print("Unrecognized Input.")
            Profile.all_page()        
        
    

def main():
    Profile.all_page()

if __name__ == "__main__":
    main()
