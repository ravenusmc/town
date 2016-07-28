class Human():

  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender 
    self.boredom = 0

  def walk(self):
    print(self.name + " is walking!")
    self.boredom += 2
    print(self.boredom)