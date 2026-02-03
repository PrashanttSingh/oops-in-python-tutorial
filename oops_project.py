class logogram:
  def __init__(self):
    self.username=''
    self.password=''
    self.login=False
    self.menu()
    
  def menu(self):
      user_input=input('''Hii! Welcome to logogram, How would you like to proceed
                          1. press 1 to signup into the app
                          2. press 2 to login into the app 
                          3. press 3 to make or write your first post
                          4. press 4 to message a friend
                          5. press any other key to exit the app''')
      if user_input =='1':
        pass
      elif user_input =='2':
          pass
      elif user_input =='3':
          pass
      elif user_input =='4':
          pass
      else:
          exit()    
          
obj=logogram()          