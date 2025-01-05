# Write a function that computes and returns the factorial of a number 
# by using a for or while loop. The factorial of a positive integer n, 
# signified by n!, is defined as the product of all integers between 1 and n, inclusive:

# n!	  Expansion	             Result
# 1!	  1	                     1
# 2!	  1 * 2	                 2
# 3!	  1 * 2 * 3	             6
# 4!	  1 * 2 * 3 * 4	         24
# 5!	  1 * 2 * 3 * 4 * 5	     120

def factorial(n):
    result = 1
    for number in range(n, 0, -1):
        result *= number

    return result

print(factorial(3))