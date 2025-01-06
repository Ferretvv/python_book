# Without running this code, what will it print? Why?

dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])  # Prints [1, 42, 3]

# dict1 is not the same as dict2. But dict() just creates a shallow copy so any changes in dict1 will be reflected in dict2

# Launch School: This code demonstrates that two dicts with equal-value objects associated with every 
# key may also share those objects. That isn't always the case, but you must understand what's happening in your code.