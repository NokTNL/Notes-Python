# For buit-in modules, just use `import`
import random

# LISTS are basically arrays, defined with `[]`
food = ['pizza', 'burger', 'pasta', 'sushi']
# To get a random item from an array:
my_choice = random.choice(food)

# Booleans
my_num = 5
print(my_num > 0) # Booleans in Python are `True`` or `False``
### if ... else
# Remember to add `:` at the end of the statement!
if (my_num > 0):
    print('Postive number')
elif (my_num < 0):
    print('Negative number')
elif (my_num == 0): # `==` is the equality operator
    print('Zero')
else:
    print ('WTF')
