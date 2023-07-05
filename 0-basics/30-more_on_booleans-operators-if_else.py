### Boolean operators
# They are `and`, `or` and `not`.
a = 1
b = 2
a == 1 and b == 3 # False
a == 1 or b == 3 # True
a == 1 and not b == 2 # False; 
# Shortcircuiting also work in Python, because `and` and `or` returns one of its operand
def say_word(str):
    print(str)
[] and say_word('and') # [] <-- this is False, so won't say the word
[] or say_word('or') # say_word('or'), because [] is False


### Truthiness (https://docs.python.org/3/library/stdtypes.html#truth-value-testing)
# When any value is used as a boolean (e.g. in `if` or `while` conditions, or with boolean operators), they will be tested for truthiness.
# ALL values are True in Python except:
# - `None`, `False`
# - 0
# - "Empty" things, e.g. '', (), [], {}

### if ... else
my_num = 5
# Remember to add `:` at the end of the statement!
if (my_num > 0):
    print('Postive number')
elif (my_num < 0):
    print('Negative number')
elif (my_num == 0): # `==` is the equality operator
    print('Zero')
else:
    print ('WTF')

### Ternary operator
# In Python it looks like an inline if...else statement
my_num2 = 9
print('Yeah' if my_num2 == 10 else 'Nah')

# Checking if list items are truthy
print(any([False, None, "Hi"])) # True
print(all([False, None, "Hi"])) # False