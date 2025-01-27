#
# Strings
#
# Strings can use single or double qoutes
print('Hello World')
print("Hello World with double quotes")
# Mulitline string """
print("""
      Hi My name is
      Tom!
      """) # All the whitespaces beyond the """ are included , including the indentations
# Escape characters
print("I want to escape a quotation mark \"")

# Strings can be concatenated together with +
my_string = "AHAHAHAHAH"
print("Hello World " + my_string + "!")
# You can even use +=
name = "John"
name += " Doe"
print(name) # John Doe

# !!! Weirdly, string literals separaed only by whitespaces will be turned into a single string literal
print("Strings" " separated" " with spaces only")

#
# Numbers
#
print(type(30)) # <class 'int'>
print(type(30.1)) # <class 'float'>
# Operators:
# - +-x/
# - % (modulus)
# ** (exponentiation)
# // (floor division, i.e. taking the floor of the division result)

# To print numbers alongside strings, (one of the ways) is to construct a string using the `str()` constructor
# NOTE: Python is strongly-typed so it does not do implicit type conversion to make you happy
print("My lucky number is " + str(7))

# The other way round, you can convert strings back to numbers
print(int("30") + int("50")) # 80
print(float("30.1") + float("50.5")) # 80.6
# NOTE: if you try to convert invalid values, it will give runtime error

# There are a few built-in functions for dealing with numbers
# abs(), min(), max(), round()
# A lot of functions require you to import `math`
from math import * # imports everything from it
# e.g. floor, ceil, sin, ....
print(floor(3.14159)) # 3

# Check a variable's type
# 1. `type()` returns the CLASS of the variable it belongs to
print(type("Hi")) # <class 'str'> ; `str` is a built-in class
print(type("Hi") == str) # True

# 2. Check using `isinstance()`
print(isinstance("Hi", str)) # True