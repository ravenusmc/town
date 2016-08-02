import random 

#Classes and other files being imported being imported
from human import Human
from car import Car
from resturant import *
from validation import *
from eat import *
from bed import *
from apartment import Apartment

#### Resturant Functions ############

def resturant(person):
  resturant = Resturant()
  waiter = Waiter()
  print("\033c")
  print(person.name + " goes into the resturant!")
  print("you see a counter or table.")
  sit = input("Where do you want to sit down?(counter or table) ")
  if sit == "counter":
    resturant.counter(person)
    waiter.greet(person) 
    flirt = input("Do you want to try and flirt with the waitress?(y/n) ")
    if flirt == "y":  # BUG: When trying to do these options, they simple don't do anything. (same in the table area)
      print("1. Smile")
      print("2. Touch hand")
      print("3. Talk")
      option = int(input("What would you like to do? "))
      if option == 1:
        person.smile(waiter)
      elif option == 2:
        person.touch(waiter) 
      elif option == 3:
        person.talkResturant(waiter)
    resturant.menu(person)
    ####
    print('You wait about five minutes and your items, which you ordered come out!')
    person.eat()
    print("The food is okay but you feel anxious about moving on!")
    print("You get up, pay your bill, and head out onto the street")
    street(person)
  elif sit == "table":
    resturant.table(person)
    waiter.greet(person)
    flirt = input("Do you want to try and flirt with the waitress?(y/n) ")
    if flirt == "y":
      print("1. Smile")
      print("2. Touch hand")
      print("3. Talk")
      option = int(input("What would you like to do? "))
      if option == 1:
        person.smile(waiter)
      elif option == 2:
        person.touch(waiter)
      elif option == 3:
        person.talkResturant(waiter)
    resturant.menu(person)
    ####
    print('You wait about five minutes and your items, which you ordered come out!')
    person.eat()
    print("The food is okay but you feel anxious about moving on!")
    print("You get up, pay your bill, and head out onto the street")
    street(person)
    

#### End of Resturant Functions ############

#### Main functions #########

def street(person):
  print("\033c")
  print("You are back out on the street.")
  print("Finally, you notice you have fifty dollars on yourself")
  choice = input("Where do you want to do?(resturant, club, office, apartments) ")
  while not validStartChoice(choice):
    choice = input("Where do you want to do?(resturant, club, office, apartments) ")
  if choice == "resturant":
    resturant(person)
  elif choice == "apartments":
    pass  # apartment(person)

def start(person):
  print("\033c")
  print("Imagine, if you will, a normal town in middle America")
  print("This town, from the outside appears perfectly normal")
  print("Yet, there is something not quite right about it...")
  print('\n')
  print("You are standing on the edge of the street.")
  print("You have no idea how you got there...")
  print('\n')
  print("There are a lot of people around you")
  print("You see a resturant behind you")
  print("You see a dance club across the street")
  print("Next to the dance club you see an office that is hiring people")
  print("Finally, you notice you have", person.money , "dollars on yourself")
  choice = input("Where do you want to go?(resturant, club, office, apartments) ")
  while not validStartChoice(choice):
    choice = input("Where do you want to go?(resturant, club, office, apartments) ")
  if choice == "resturant":
    resturant(person)
  elif choice == "apartments":
    pass  # apartment(person)

def config():
  print("\033c")
  print("To start, I need some data ")
  name = input("What is your name? ")
  age = int(input("what is your age: "))
  while not validConfig(age):
    age = int(input("what is your age: "))
  gender = input("What is your gender? ")
  person = Human(name, age, gender)
  print("Here we go!!!")
  start(person)

def main():
  print("---------------------------")
  print("Welcome to the Object town!")
  print("---------------------------")
  choice = input("Would you like to play?(y/n) ")
  while not validMain(choice):
    choice = input("Would you like to play?(y/n) ")
  if choice == 'y':
    config()
  else:
    input("Thank you for coming by!")

main()