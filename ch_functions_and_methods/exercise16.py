def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# Identify all of the function names and parameters present in the code. 
# Include the line numbers for each item identified.

# function names = multiply (1, 9), get_num(4, 7, 8), float(5), input(5), print(10)
# parameters     = left right (1, 2), prompt(4, 5)

# float, input, and print are built-in functions