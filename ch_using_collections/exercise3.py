# Write Python code to create a new tuple from (1, 2, 3, 4, 5). 
# The new tuple should be in reverse order from the original. 
# It should also exclude the first and last members of the original. 
# The result should be the tuple (4, 3, 2).

old_tuple = (1, 2, 3, 4, 5)
new_tuple = old_tuple[-2:0:-1]
print(new_tuple)
# I originally tried .reverse() but tuples are immutable
# If I wanted to, here's another method:
my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
my_list.reverse()
result = tuple(my_list[1:4])
print(result)  