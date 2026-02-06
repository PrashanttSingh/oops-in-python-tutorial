class animal:
  def __init__(self,name):
    animal.self=name

  def speak(self):
    print(f'{animal.self} speaks...')

class dog(animal):
  def speak1(self):
    print(f'{animal.self} barks...')


# animal=animal('buddy')
# animal.speak()          
dog=dog('dog')
dog.speak()