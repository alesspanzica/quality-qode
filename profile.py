"""
Profile()
This is the class that represents the Profile object. 

    Profile() attributes:
    -

    Profile() methods:

        all_page(dict): Prepares CLI to interact with profiles, organizing all known profiles

        profile_page(profile, dict): Enables user to view and edit profile information in CLI

"""

from user import User

class Profile:
    user_profiles = None

    def profile_page(profile, dict):
        inp2 = input("Actions: View or Edit " + str(profile) + ", or type 'Back' to return to Profiles List\n") #CLI input
        if inp2 == "Back":
            Profile.all_page(dict)

        elif inp2 ==  "View": #prints all User variables and their values
            for property, value in vars(profile).items():
                print(property, ":" , value)
            Profile.profile_page(profile, dict)

        elif inp2 == "Edit": #broken!! back-end stuff
            vardict = vars(profile).items()
            for property, value in vardict:
                print(property, ":" , value)
            inp3 = input("What field would you like to change?\n")
            if inp3 is property in vardict: #specifically broken
                inp4 = input("Enter new value:\n")
                property.value = inp4
            else:
                print("Unrecognized Input.")
                
            Profile.profile_page(profile, dict) #return to CLI for 
        
        elif inp2 == "Exit":
            exit()
        
        else:
            print("Unrecognized Input.")
            Profile.profile_page(profile, dict)

    def all_page(dict):
        temp = list(dict.keys()) #get User class variables in list
        inp = input("Actions: View : " + str(temp) + "\n")
        if inp in temp: #if valid profile selected...
            Profile.profile_page(dict[inp], dict)
        elif inp == "Exit":
            exit()
        else:
            print("Unrecognized Input.")
            Profile.all_page(dict)        
        
    

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
    person2 = User()
    person2.name = "Joe"
    allprofiles = {str(person):person, str(person2):person2}
    Profile.all_page(allprofiles)

if __name__ == "__main__":
    main()
