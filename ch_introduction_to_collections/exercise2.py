# Can you write some code to change the value 'bye' in the following tuple to 'goodbye'?
stuff = ('hello', 'world', 'bye', 'now')
# I don't t hink so since tuples are immutable
# Launchschool solution is converting tuple into a list
# and reassigning the element to the new value
stuff = list(stuff)
stuff[2] = 'goodbye'
stuff = tuple(stuff)