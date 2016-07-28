class Car():

  def __init__(self, model):
    self.model = model

  def start(self, person):
    if person.age >= 16:
      print("Car Started")
    else:
      print("You need to be at least 16 to drive!")