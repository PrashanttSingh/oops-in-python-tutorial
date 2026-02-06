# class parent:
#  def __init__(self,name):
#     parent.self=name

#  def goods(self):
#     print(f'{parent.self} has good handwritting...')  

# class child(parent):
#   def goods(self):
#     print(f'yes  my dad says true i({parent.self}) has good handwritting...')

# # parent=parent('alice')    
# # parent.goods()
# child=child('alice')
# child.goods()
#----------------------------------------------------------------------------

#multi-level inheritence
class grandparent:
  def __init__(self,color):
    self.color=color

  def loves(self):
    print(f'grandparents love {self.color} color')

class parent(grandparent):
  def does(self):
    print(f'parents love just like grandparents {self.color} color ')

class child(parent):
  def do(self):
    print(f'child loves same colour as the parents love the {self.color} color')

child=child('blue')
child.loves() 
child.do() 
child.does()
#-----------------------------------------------------------------------------------