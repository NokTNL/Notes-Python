#
# Booleans
#
print(type(True)) # <class 'bool'>

### Boolean operators
# They are `and`, `or` and `not`.
a = 1
b = 2
a == 1 and b == 3 # False
a == 1 or b == 3 # True
a == 1 and not b == 2 # False; 
# `and` and `or` are short-circuit operators, i.e. they return one of its operands
def say_word(str):
    print(str)
[] and say_word('and') # [] <-- this is False, so won't say the word
[] or say_word('or') # say_word('or'), because [] is False


### Truthiness (https://docs.python.org/3/library/stdtypes.html#truth-value-testing)
# In a context expecting a boolean, all values are evaluated as `True` except:
# - `None`, `False`
# - 0
# - "Empty" things, e.g. '', (), [], {}

### if ... else
# No need parenthesis around conditions
# Remember to add `:` at the end of the statement!
my_num = 5
if my_num > 0:
    print('Postive number')
elif my_num < 0:
    print('Negative number')
elif my_num == 0:
    print('Zero')
else:
    print ('WTF')

#
# Ternary operator
#
# In Python it looks like an inline if...else statement
my_num2 = 9
print('Yeah' if my_num2 == 10 else 'Nah')

# Checking if some / all list items are truthy
print(any([False, None, "Hi"])) # True
print(all([False, None, "Hi"])) # False

#
# While loop
#
i = 1
while i <= 10:
    print(f"while i is {i}")
    i += 1

#
# For loop
#
# In Python, for loops always loop over a list
for number in [1, 3, 5, 7]:
    print(f"for number is {number}")
# You can retreive the index as well
for i, number in enumerate([1, 3, 5, 7]): # index, number is destructuring the tuple returned from `enumberate`
    print(f"for index is {i} and number is {number}")
# Probably easier to just use range(), which produces a list of [0, stop_index)
for i in range(6):
    print(f"for i is {i} in range(6)")
# `break` and `continue` are available for `while` and `for` loops