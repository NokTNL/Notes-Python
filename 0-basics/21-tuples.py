# Tuples are similar to lists but are IMMUTABLE once created
myTuple = 1, 3, 5 # (1, 3, 5) means the same
print(type(myTuple)) # <class 'tuple'>
nested_tuple = 1, (2, 3, 4) # Or (1, (2, 3, 4))
# Accessing items with []
print(myTuple[0:2]) # (1, 3)
# Joining with `+`
print((1,2) + (3,4)) # (1, 2, 3, 4)

