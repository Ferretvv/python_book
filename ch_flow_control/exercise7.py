# Write a function that takes a single integer argument 
# and prints a message that describes whether:
# the value is between 0 and 50 (inclusive)
# the value is between 51 and 100 (inclusive)
# the value is greater than 100
# the value is less than 0

def single_integer(number):
    if number < 0:
        print(f"{number} is less than 0")
    elif number > 100:
        print(f"{number} is greater than 100")
    elif number > 50:
        print(f"{number} is between 51 and 100 inclusive")
    else:
        print(f"{number} is between 0 and 50 inclusive")


single_integer(0)
single_integer(25)
single_integer(50)
single_integer(75)
single_integer(100)
single_integer(101)
single_integer(-1)