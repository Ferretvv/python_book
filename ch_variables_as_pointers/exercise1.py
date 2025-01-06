# In your own words, explain the difference between these two expressions.

my_object1 == my_object2        # This is asking if both variavles have the same elements.
# Launch School: Compares both to see if equal. Considered equal when  have the same value or state. 
# In the case of collections, two collections are equal when they have the same elements.
# Value Equality


my_object1 is my_object2        # This is asking if both variables are the same 
# Launch School: checks two variables to see whether they reference the same object. An object is the same 
# as another object if both are stored at the same location in memory. In particular, that means we can say 
# that my_object1 and my_object2 share the referenced object or that my_object1 and my_object2 are aliases for the same object.
# Object Equality