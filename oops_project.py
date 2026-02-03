import time

class logogram:
  def __init__(self):
    self.username=''
    self.password=''
    self.login=False
    self.menu()
    
  def menu(self):
      time.sleep(1)
      user_input=input('''Hii! Welcome to logogram, How would you like to proceed
                          1. press 1 to signup into the app
                          2. press 2 to login into the app 
                          3. press 3 to make or write your first post
                          4. press 4 to message a friend
                          5. press any other key to exit the app ''')
      time.sleep(1)
      if user_input =='1':
        print('Wait! Getting things ready for you')
        time.sleep(2)
        self.signup()
      
      elif user_input =='2':
        print('Wait! Getting things ready for you')
        time.sleep(2)
        self.signin()
        
      elif user_input =='3':
          print('Wait! Getting things ready for you')
          time.sleep(2)
          self.my_post()
      elif user_input =='4':
          print('Wait! Getting things ready for you')
          time.sleep
          pass
      else:
          time.sleep(0.5)
          print('Thankyou for using logogram,see you soon')
          exit()    
  def signup(self):
    email=input('Enter your email-')
    time.sleep(0.5)     
    pwd=input('Enter your Password-')
    self.username=email
    self.password=pwd
    print('\n')
    self.menu()
    
  def signin(self):
    time.sleep(1)
    if self.username=='' and self.password=='':
      print('Plese signup first by pressing 1 in the main menu')
    else:
      usernme=input('enter your email or username-')
      time.sleep(.5)
      pwd=input('enter your password-')
      if self.username==usernme  and pwd==self.password:
        time.sleep(1.7)
        print('login successfull')
        self.login=True
      else:
        print('something is wrongly written')  
    print('\n') 
    time.sleep(4) 
    self.menu()  
    
  def my_post(self):
     if self.login==True:
       time.sleep(1)
       input('plese write your post Description-')
     else:
       time.sleep(1)
       input('OOPS! look like your are not signed in😶')
     print('\n') 
     self.menu() 
     
         
obj=logogram()        