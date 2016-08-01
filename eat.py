from resturant import *

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
    input("You move back out onto the street.")
    # street(person)
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
    input("You move back out onto the street.")
    # street(person)
    

#### End of Resturant Functions ############