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