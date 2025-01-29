#
# List
#
# A list is collection of item (like an "array"), defined with `[]`
food = ['pizza', 'burger', 'pasta', 'sushi']
print(type(food)) # <class 'list'>
# Check length with len()
print(len(food)) # 4
# Item access using []
print(food[1]) # burger
print(food[-1]) # sushi; NEGATIVE index count from FIRST element as zero
print(food[1:3]) # ['burger', 'pasta']; RANGE index returns a sub-array; it is [1, 3) (i.e. includes 1 and STOPS BEFORE 3)
print(food[1:10]) # ['burger', 'pasta', 'sushi']; range indices bigger than the maximum are all treated as "beyond the end"
print(food[:2]) # ['pizza', 'burger']; equivalent to [0:2]
print(food[2:]) # ['pasta', 'sushi']; equivalent to [2:4]
# Mutating items by direct assignment
food[1] = 'ramen' 
print(food[1]) # ramen
# Checking if a value is in a list
print('pizza' in food) # True
print('salad' in food) # False
# list.index(): returns the index of the FIRST matching item
print(food.index('pasta')) # 2
# print(food.index('IIUI')) # ValueError: 'IIUI' is not in list


# List manipulation
boys = ['Tom', 'Paul', 'Julian']

### append(): add ONE item to the end of the array 
boys.append('John') 
print(boys) # ['Tom', 'Paul', 'Julian', 'John']
# The opposite is list.pop()

### extend(): joining an array to the end
boys.extend(['Karl', 'Sam']) 
print(boys) # ['Tom', 'Paul', 'Julian', 'John', 'Karl', 'Sam']
# You can also use `+` on lists! (and '+=' by extension)
boys += ['HA']
print(boys) # ['Tom', 'Paul', 'Julian', 'John', 'Karl', 'Sam', 'HA']
# !!! If you want to extend with a single string array (e.g. 'Sam') but forget the `[]`, the string will be added AS A LIST --> 'S', 'a', 'm'

### remove(): remove the first item that matches the value from the array 
boys.remove('HA')
print(boys) # ['Tom', 'Paul', 'Julian', 'John', 'Karl', 'Sam']

### insert(): add an item at the specified index (i.e. it will appear at that index and push other items to the right)
boys.insert(2, 'INSERTED')
print(boys) # ['Tom', 'Paul', 'INSERTED', 'Julian', 'John', 'Karl', 'Sam']

### To insert multiple items as a list, you select a sub-array and then mutate it:
boys[3:3] = ['INSERTED2', 'INSERTED3'] # [3:3] is an EMPTY array, so you are just selecting a POSITION!
print(boys) # ['Tom', 'Paul', 'INSERTED', 'INSERTED2', 'INSERTED3', 'Julian', 'John', 'Karl', 'Sam']
# You can also choose a non-empty sub-array; the selected items will be replaced

### sort()
# It sorts using "<", so an all-string array will be sorted alphabetically, and an number array numerically
# Sorting a mixed str and number array will give error
numbers = [1, 5, 3, 2, 4]
numbers.sort()
print(numbers) # [1, 2, 3, 4, 5]
words = ['banana', 'apple', 'carrot']
words.sort()
print(words) # ['apple', 'banana', 'carrot']
# To keep the original array, you can 
# 1. use the global sorted() method
print(sorted([4, 1, 3, 2])) # [1, 2, 3, 4]
# 2. Make a copy of the original, and then sort the copy
list1 = [4, 1, 3, 2]
list2 = list1[:] # a sub-array from end to end --> the whole array
list2.sort()
print(list1, list2) # [4, 1, 3, 2] [1, 2, 3, 4]

#
# Tuples
#
# Tuples are similar to lists but are IMMUTABLE once created
myTuple = 1, 3, 5 # (1, 3, 5) means the same
print(type(myTuple)) # <class 'tuple'>
nested_tuple = 1, (2, 3, 4) # Or (1, (2, 3, 4))
# Accessing items with []
print(myTuple[0:2]) # (1, 3)
# Joining with `+`
print((1,2) + (3,4)) # (1, 2, 3, 4)


