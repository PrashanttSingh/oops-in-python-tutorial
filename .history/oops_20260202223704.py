#initating a class
class phone:
  #constructor
  def __init__(self):
    phone.number=1
    phone.color='red'
    phone.price=20000
    phone.weight='200g'
    
  def owner(self,name):
    print(f'the phone owner is {name}')  

samsung=phone()
print(samsung.color)    