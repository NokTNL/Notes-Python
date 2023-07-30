# LISTS are basically arrays, defined with `[]`
food = ['pizza', 'burger', 'pasta', 'sushi']
print(type(food)) # <class 'list'>
# Check length with len()
print(len(food)) # 4
# Item access using []
print(food[1]) # burger
print(food[-1]) # sushi; NEGATIVE index count from FIRST element as zero
print(food[1:3]) # ['burger', 'pasta']; RANGE index returns a sub-array; includes 1 and STOPS BEFORE 3
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
# An alternative is '+='
boys += ['HA']
print(boys) # ['Tom', 'Paul', 'Julian', 'John', 'Karl', 'Sam', 'HA']
# !!! If you want to extend with a single string array (e.g. 'Sam') but forget the `[]`, the string will be added AS A LIST --> 'S', 'a', 'm'

### Joining arrays with `+`
print([1, 'A'] + [2, 'B']) # [1, 'A', 2, 'B']

### remove(): remove an item from the array that matches the value
boys.remove('HA')
print(boys) # ['Tom', 'Paul', 'Julian', 'John', 'Karl', 'Sam']

### insert(): an ONE item at the specified index (i.e. it will appear at that index and push other items to the right)
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
