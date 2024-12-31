# This question may be a little challenging if your math skills are rusty.
# Don't be afraid to take advantage of the hints. Try your best to solve the problem,
# but don't feel compelled to complete it if you become frustrated.
# Use the REPL and the arithmetic operators to extract the individual digits of 4936:
number = 4936
ones = number % 10
print(ones)               #6
number = number // 10
print(number)             #493
tens = number % 10
print(tens)               #3
number = number // 10
print(number)             #49
hundreds = number % 10
print(hundreds)           #9
thousands = number // 10
print(thousands)          #4