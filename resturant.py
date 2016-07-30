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
    print("5. Cola-$1.00")
    print("2. Coffee-$1.00")
    print("3. Pancakes-$2.00")
    print("4. Burger-$3.00")
    select = int(input("What do you want? "))


class Waiter(Resturant):

  def __init__(self):
    self.love = 0

  def greet(self, human):
    if human.gender == "male":
      print("Well Hello there Mr!")
      print("What are we having today?")
    elif human.gender == "female":
      print("Well Hello there Madam!")
      print("What do you want today?")

