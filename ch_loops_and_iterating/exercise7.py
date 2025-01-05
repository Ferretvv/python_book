# Write a find_integers function that returns a list of all the integers from my_tuple:
my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)

def find_integers(things):
    return [ element
             for element in things
             if type(element) is int ]


integers = find_integers(my_tuple)
print(integers)  

# Non list comprehension:

def find_integers(things):
    result = []
    for element in things:
        if type(element) is int:
            result.append(element)
    return result