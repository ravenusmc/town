class Resturant():

  def __init__(self):
    self.tab = 0

  def counter(self, human):
    print(human.name + " sits at the counter!")

  def table(self, human):
    print(human.name + " sits at the table!")

class Waiter(Resturant):

  def __init__(self):
    self.love = 0

  def greet(self, human):
    print("Hello " + human.name)