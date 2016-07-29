from human import Human
from car import Car


def main():
  print("---------------------------")
  print("Welcome to the Object town!")
  print("---------------------------")

name = input("What is your name? ")
age = int(input("What is your gender? "))


person = Human(name, 13)
person.walk()
car = Car("Prius")
car.start(person)

print