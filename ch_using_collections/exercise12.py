# Write some code that determines and prints whether the number 3 appears inside each of these lists:

numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']

# print(3 in numbers1)
# print(3 in numbers2)
# print(3 in numbers3)
# print(3 in numbers4)
# print(3 in numbers5)      

def is_3_in(list):
    print(3 in list)

is_3_in(numbers1)
is_3_in(numbers2)
is_3_in(numbers3)
is_3_in(numbers4)
is_3_in(numbers5)     # This returns true because (3 == 3.0)