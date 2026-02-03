import time

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
      time.sleep(1)
      if user_input =='1':
        print('Wait! Getting things ready for you')
        time.sleep(2)
        self.signup()
      
      elif user_input =='2':
        print('Wait! Getting things ready for you')
        time.sleep(2)
        pass
      elif user_input =='3':
          print('Wait! Getting things ready for you')
          time.sleep(2)
          pass
      elif user_input =='4':
          print('Wait! Getting things ready for you')
          time.sleep
          pass
      else:
          time.sleep(0.5)
          print('Thankyou for using logogram,see you soon')
          exit()    
  def signup(self):
    email=input('Enter your email')
    time.sleep(0.5)     
    pwd=input('Enter your Password')
    self.username=email
    self.password=pwd
    self.menu
    
    
obj=logogram()        