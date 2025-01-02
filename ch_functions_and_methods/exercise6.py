# What does the following code print?

def scream(words):
    words = words + '!!!!'
    return
    print(words)

scream('Yipeee')

# Doesn't print anything. return on line 5 terminates the function
# before it prints anything