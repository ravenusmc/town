import random 

#Classes and other files being imported being imported
from human import Human
from car import Car
from resturant import *
from validation import *
from eat import *
from bed import *
from apartment import Apartment

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