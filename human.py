class Human():

  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.boredom = 0

  def walk(self):
    print(self.name + " is walking!")
    self.boredom += 2
    print(self.boredom)