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
    self.dating = False

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

  def talkResturant(self, waiter):
    if self.gender == "male" and waiter.id == "waiter":
      info = input("What do you want to learn about 'town', 'work', 'bed', 'love' or 'done' ")
      while True:
        if info == "town":
          print("'What town is this?' You ask.")
          print("'Why this is MorrisVille!' The Waitress responds")
          print("The waitress smiles as you look her over.")
        elif info == "work":
          print("'Is there a place that I can get some work?'")
          print("'Of course there is sir! Just hold over to the office building!'")
          print("'They are always looking for help and pay well'")
        elif info == "bed":
          print("'Is there a place that I can get a bed to stay here?'")
          print("'Oh yes, head to the apartments. However, they are expensive'")
          print("'Not sure about the amount of money you have but you may need a job...'")
        elif info == "love":
          print("'Any ideas on where I can find a date here in this town?'")
          if waiter.love >= 8:
            print("'Why you can date me! I have been looking for a partner!'")
            date = print("'Do you want to date me?'(y/n) ")
            if date == 'y':
              self.dating = True
            elif date == 'n':
              print("The waitress hits you!")
              print("'Now you hurt my feelings!'")
              waiter.love -= 3
          elif waiter.love < 8:
            print("'You can try heading to the club! Best of luck to you!'")
        elif info == "done":
          break 
        info = input("What do you want to learn about 'town', 'work', 'living space', 'love'or 'done' ")
    elif self.gender == "female" and waiter.id == "waiter":
      info = input("What do you want to learn about 'town', 'work', 'bed', 'love'or 'done' ")
      while True:
        if info == "town":
          print("'What town is this?' You ask.")
          print("'Why this is MorrisVille!' The Waiter responds")
          print("The waiter smiles as you look her over.")
        elif info == "work":
          print("'Is there a place that I can get some work?'")
          print("'Of course there dear! Just hold over to the office building!'")
          print("'They are always looking for help and pay well'")
        elif info == "bed":
          print("'Is there a place that I can get a bed to stay here?'")
          print("'Oh yeah, head to the apartments. However, they are expensive'")
          print("'Not sure about the amount of money you have but you may need a job...'")
        elif info == "love":
          print("'Any ideas on where I can find a date here in this town?'")
          if waiter.love >= 8:
            print("'Why you can date me! I have been looking for a partner!'")
            date = print("Do you want to date me?(y/n) ")
            if date == 'y':
              self.dating = True
            elif date == 'n':
              print("The waiter hits you!")
              print("'Now you hurt my feelings!'")
              waiter.love -= 3
          elif waiter.love < 8:
            print("'You can try heading to the club! Best of luck to you!'")
        elif info == "done":
          break 
        info = input("What do you want to learn about 'town', 'work', 'living space', 'love'or 'done'")


