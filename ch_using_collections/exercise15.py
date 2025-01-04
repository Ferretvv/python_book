pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

keys = pets.keys()
del pets['Dog']
pets['Snake'] = 'Sssss'
print(keys)

# Without running the code, what values will be printed by line 10?
# 'Cat', 'Bird', 'Snake'

# Since dict.keys returns a dictionary view object, any changes made 
# to the dictionary after you call the keys method will be reflected in
# dictionary view referenced by keys immediately.

