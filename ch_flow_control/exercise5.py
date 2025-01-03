# What does this code output, and why?

def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([])

# Prints Empty since there's nothing in the list it's falsy. if my_list 
# is as asking if its truthy but it isn't so it goes on to else statement