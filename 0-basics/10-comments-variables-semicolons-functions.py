# This is a single line comment
##### This also works
""" This is a multi-line comment
    This is the second line"""

"""
- VARIABLES are declared without a keyword
- By convention, Python variables are in snake_case
- Variable names cannot:
    - Start with a number (1num)
    - Include !, %
    - Be equal to Python keywords
"""
my_string = 'Hello World'
my_num = 10
# Variables can be reassigned later
my_string = "HAHAHAHAH"
print(my_string) # HAHAHAHAH

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