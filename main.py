import random 

#Classes being imported
from human import Human
from car import Car
from resturant import Resturant


#### Resturant Functions ############

def resturant(person):
  resturant = Resturant()
  print(person.name + " goes into the resturant!")
  print("you see a counter or table.")
  sit = input("Where do you want to sit down?(counter or table) ")
  if sit == counter:
    resturant.counter(person)
  elif sit == table:
    resturant.table(person)
    


#### End of Resturant Functions ############

def start(person):
  print("\033c")
  print("You are standing on the edge of the street.")
  print("You have no idea how you got there...")
  print('\n')
  print("There are a lot of people around you")
  print("You see a resturant behind you")
  print("You see a dance club across the street")
  print("Next to the dance club you see an office that is hiring people")
  print("Finally, you notice you have fifty dollars on yourself")
  choice = input("Where do you want to do?(resturant, club, office) ")
  if choice == "resturant":
    resturant(person)


def config():
  print("\033c")
  print("To start, I need some data ")
  name = input("What is your name? ")
  age = int(input("what is your age: "))
  gender = input("What is your gender? ")
  person = Human(name, age, gender)
  print("Here we go!!!")
  start(person)

def main():
  print("---------------------------")
  print("Welcome to the Object town!")
  print("---------------------------")
  choice = input("Do you want to use it?(y/n) ")
  if choice == 'y':
    config()
  else:
    print("Thank you for coming by!")

# person.walk()
# car = Car("Prius")
# car.start(person)

main()