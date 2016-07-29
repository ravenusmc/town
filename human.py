class Human():

  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender 
    self.life = 15
    self.hunger = 14
    self.boredom = 0
    self.bathroom = 0
    self.money = 50

  def walk(self):
    print(self.name + " is walking!")
    self.hunger -= 2
    if self.hunger <= 5:
      print("You are getting hungry, you should eat soon!")

  def eat(self):
    print(self.name + " is eating")
    self.hunger += 2 
    self.bathroom += 2 
    if self.bathroom >= 7:
      print("You need to find a bathroom!")

  def bathroom(self):
    print(self.name + " went to the bathoom!")
