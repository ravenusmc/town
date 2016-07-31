#All of the validations for my object town will be in here. 

#### Validations for Main Function
def validMain(choice):
  if choice == "y" or choice == "n":
    return True
  else:
    return False 

### Validations for Config Function 
def validConfig(age):
  if age <= 0 or age >= 125:
    return False
  else:
    return True 