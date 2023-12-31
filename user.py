#<<<<<<< HEAD:User.py
'''
User()
This is the class that represents the User object. All fields are required 
when a user is registering. 
 
    User() attributes:
        username: User's chosen screen name [STRING]
        name: User's name [STRING]
        phone_number: User's phone number [STRING]
        address: User's address [STRING]
        position: User's position in the company, controls what tasks they are allowed
        to work on [INTEGER]
        email: User's email [STIRNG]
        manager: The user/manager that the current user reports to [USER object]
          -> every user has an associated manager, in the backend implmeneted, the 
          hierarchy will be implemented
        bio: Self bio user can create about themselves. To be displayed on their profile [STRING]
        picture-filename: Profile photo for the user [STRING]

    User() methods:
        update_pic(): Allows the user to update their profile photo.
        update_bio(): Allows the user to update their bio in their profile. 
        __str__(): Used to get the name of a user profile. 
'''
class User:
    bio = ""
    picture_filename = ""
    
    def __init__(self, username, name, phone_number, address, 
                email, position, manager, password):
      self.username = username
      self.name = name
      self.phone_number = phone_number
      self.address = address
      self.email = email
      self.position = position
      self.manager = manager
      self.password = password

    def update_pic(self, pic_filename):
      self.picture_filename = pic_filename

    def update_bio(self, bio):
      self.bio = bio

    def __str__(self):
      return format(self.name)  
