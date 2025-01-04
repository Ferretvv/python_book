# Which of the following values can't be used as a key in a dict object, and why?
'cat'
(3, 1, 4, 1, 5, 9, 2)
['a', 'b']              # Is a list. Mutable types can't be used as dict keys
{'a': 1, 'b': 2}        # Is a dict. Mutable types can't be used as dict keys
range(5)
{1, 4, 9, 16, 25}       # Is a set. Mutable types can't be used as dict keys
3
0.0
frozenset({1, 4, 9, 16, 25})

# Dict keys need to be mutable and hashable