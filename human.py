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

  def smile(self, waiter):
    print("You smiled!")
    waiter.love += 2
    print(waiter.love)

  def touch(self, waiter):
    if self.gender == "male":
      print("You reach out and touch the waitresses hand ")
      if waiter.love <= 8:
        print("The waitress slaps your hand")
        print("'What do you think your doing Mr.' She says. 'I barely know you!'")
        print("You decide to continue to look at the menu.")
      else:
        print("The waitress holds on to your hand. You can feel you two have a connection!")
    elif self.gender == "female":
      print("You reach out and touch the waiters hand.")
      if waiter.love <= 8:
        print("The waitress slaps your hand")
        print("'What do you think your doing Mr.' She says. 'I barely know you!'")
        print("You decide to continue to look at the menu.")
      else:
        print("The waitress holds on to your hand. You can feel you two have a connection!")
