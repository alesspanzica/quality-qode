class User():
    def __init__(self):
      self.username = ""
      self.name = ""
      self.phone_number = ""
      self.address = ""
      self.email = ""
      self.position = ""
      self.manager = ""
      self.bio = ""
      self.picture = ""

    def __str__(self):
      return format(self.name)  
