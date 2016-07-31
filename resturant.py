class Resturant():

  def __init__(self):
    self.tab = 0

  def counter(self, human):
    print(human.name + " sits at the counter!")

  def table(self, human):
    print(human.name + " sits at the table!")

  def menu(self, human):
    print("You look at the menu: ")
    print("1. Tea-$1.00")
    print("2. Cola-$1.00")
    print("3. Coffee-$1.00")
    print("4. Pancakes-$2.00")
    print("5. Burger-$3.00")
    select = int(input("What do you want? "))
    if select == 1:
      print("You ordered some tea.")
      print("'Well your tea will be right out!")
      human.money -= 1
    elif select == 2:
      print("You ordered some cola!")
      print("'Well your cola will be right out!")
      human.money -= 1
    elif select == 3:
      print("You ordered some coffee!")
      print("'Well your coffee will be right out!")
      human.money -= 1
    elif select == 4:
      print("You ordered some Pancakes!")
      print("'Well your pancakes will be right out!")
      human.money -= 2
    elif select == 5:
      print("You ordered a Burger!")
      print("'Well your burger will be right out!")
      human.money -= 3 

class Waiter(Resturant):

  def __init__(self):
    self.love = 0
    self.id = "waiter" 

  def greet(self, human):
    if human.gender == "male":
      print("Well Hello there Mr!")
      print("What are we having today?")
    elif human.gender == "female":
      print("Well, Hello there Madam!")
      print("What do you want today?")

