# f-strings is an easy way to insert values into a string
# placeholders are inside `{}`
my_num = 25
print(f"I'm {my_num} years old!") # numbers are converted to string automatically

# Strings are immutable
# 'abcde'[1] = 'z' # TypeError: 'str' object does not support item assignment

# String methods
# They all return a new string and not modifying the original string
print("beau".upper()) # BEAU
print("BeAu".lower()) # beau
print("BeAu Person".title()) # Beau Person --> title case
print('Beau'.islower()) # False
# returns the LOWEST index if the substring
print("beau".find("ea")) # 1
# ...etc

# Strings work like lists in Python, so you can:
# - Access a character with index
print('abcde'[2]) # c
print('abcde'[-1]) # e
print('abcde'[1:3]) # bc
print('abcde'[:3]) # abc
print('abcde'[3:]) # de
# - Check its length with the global method len()
print(len("Beau")) # 4
# `in` operator for checking substring
print('au' in 'Beau') # True