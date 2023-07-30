# Strings concantenation can be done with +
my_string = "AHAHAHAHAH"
print("Hello World " + my_string + "!")
# NOTE: You CAN'T concat NUMBERS to strings using `+`

# Alternatively, use f-strings (similar to Javascript template literals)
# placeholders are inside `{}`
# NOTE: In f-strings you can use NUMBERS and it will be converted to a string for you
my_num = 25
print(f"I'm {my_num} years old!")

# Strings are immutable
'abcde'[1] = 'z' # TypeError: 'str' object does not support item assignment

# String methods
# They all return a new string and not modifying the original string
print("beau".upper()) # BEAU
print("BeAu".lower()) # beau
print("BeAu Person".title()) # Beau Person --> title case
print('Beau'.islower()) # False
# ...etc

# Strings work like arrays in Python, so you can:
# - Access a character with index
print('abcde'[2]) # c
print('abcde'[-1]) # e ; NEGATIVE indexes count from the reverse
print('abcde'[1:3]) # bc ; A RANGE index SLICES the string, this means includes 1 and STOPS BEFORE 3
print('abcde'[:3]) # abc
print('abcde'[3:]) # de
# - Check its length with the global method len()
print(len("Beau")) # 4

# `in` operator for checking substring
print('au' in 'Beau') # True