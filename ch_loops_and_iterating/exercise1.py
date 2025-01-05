# The following code causes an infinite loop (a loop that never stops iterating). Why?
counter = 0

while counter < 5:
    print(counter)  # Counter will always be 0 (less than 5)