class Apartment():

  def __init__(self):
    self.rooms = 3

  def available(self, human):
    if human.gender == "male":
      print("She says: 'we have three rooms available")
      bed = input("Would you want to live here?(y/n) ")
      if bed == 'y' and human.money >= 75:
        print("The rooms are $75!")
        print("Your money: $" + human.money)
        if human.money >= 75:
          print("Well it appears you do not have enough money!")   
          print("She says: 'I would recommend heading over to the office building'")
          print("'and seeing about getting a job there.' ")
        
      elif bed == 'n':
        print("well there is no where else in town to go!")
    elif human.gender == "female":
      print("She says: 'we have three rooms available")
      bed = input("Would you want to live here?(y/n) ")
      if bed == 'y' and human.money >= 75:
        print("Well it appears you do not have enough money!")
        print("Your money: $" + human.money)
        print("She says: 'I would recommend heading over to the office building'")
        print("'and seeing about getting a job there.' ")
        print("The rooms are $75!")
      elif bed == 'n':
        print("well there is no where else in town to go!")

class Host():

  def __init__(self):
    self.love = 0 

  def greet(self, human):
    if human.gender == "male":
      print("You see a women sitting at a desk")
      print("The women looks up at you and smiles")
      print("You smile back")
    elif human.gender == "female":
      print("You see a man sitting at a desk")
      print("The man looks up at you and smiles")
      print("You smile back")
    
