#single or basic inheritence
class parent:
  def __init__(self,name):
    parent.self=name

  def goods(self):
    print(f'{parent.self} has good handwritting...')  

class child(parent):
  def goods(self):
    print(f'yes  my dad says true i({parent.self}) has good handwritting...')

# parent=parent('alice')    
# parent.goods()
child=child('alice')
child.goods()
#----------------------------------------------------------------------------