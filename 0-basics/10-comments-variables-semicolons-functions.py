# This is a single line comment
##### This also works
""" This is just a multi-line string
    But can be used as comments as well
"""

# - VARIABLES are declared without a keyword
# - By convention, Python variables are in snake_case
# - Variable names cannot:
    # - start with a number (1num)
    # - include !, %
    # - be Python keywords
my_string = 'Hello World'
my_num = 10
# Variables can be reassigned later
my_string = "HAHAHAHAH"
print(my_string) # HAHAHAHAH
# Python uses dynamic types so variables can be reassigned a value with a different type
my_string = 11
print(type(my_string)) # <class 'int'>

# SEMICOLONS are NOT needed in Python; A new line breaks a statement
# However, you can use semicolons if you want to inlcude two statements in one line:
a = 1; b = 2

# FUNCTIONS are declared with the keyword `def`, followed by the function name with `:`
# Function body is INDENTED:
# - Indentations mean BLOCKS in Python; you can't randomly use them like in some other languages
# - The number of space characters used doesn't matter (it's FOUR space by convention)
def addNum(num1, num2):
    return num1 + num2

# Calling the function
sum = addNum(1, 2)
print(sum) # 3

# We can use default arguments as well, but they must go LAST
# Named arguments also possible
def addNumWithDefault(num1, num2 = 0):
    return num1 + num2
print(addNumWithDefault(num1=3)) # 3; 3 + 0 = 0
