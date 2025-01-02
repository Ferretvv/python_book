# Which of the identifiers in the following program are
# function names? Which are method names? Which are built-in functions?

def say(message):
    print(f'==> {message}')

string1 = input()
string2 = input()

say(max(string1.upper(), string2.lower()))

# function names:
# - say, print, input(), max, .uppuer(), .lower()

# method names:
# - .upper(), .lower()

# built in functions
# print, max