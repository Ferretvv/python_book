my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

# Given the above code, answer the following questions and explain your answers:

# Are the lists assigned to my_list and another_list equal?
# Yes. Both lists with the same elements

# Are the lists assigned to my_list and another_list the same object?
# No. The list contructor creates a new object

# Are the nested lists at index 3 of my_list and another_list equal?
# Yes. They are both lists that have the same elements

# Are the nested lists at index 3 of my_list and another_list the same object?
# Yes. The list contructor creates a shallow copy of the iterable passed
# as an argument. Shallow copies don't create new nested lines. Instead,
# only a reference to the nested list gets copied
