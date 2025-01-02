# Write a program that uses a multiply function to multiply 
# two numbers and returns the result. Ask the user to enter 
# the two numbers, then output the numbers and result as a simple equation.

num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))

def multiply(x, y):
    return x * y


product = multiply(num1, num2)
print(f"{num1} * {num2} = {product: .2f}")

# Launch shool's solution: 

def multiply(left, right):
    return left * right

def get_number(prompt):
    entry = input(prompt)
    return float(entry)

first_number = get_number('Enter the first number: ')
second_number = get_number('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')