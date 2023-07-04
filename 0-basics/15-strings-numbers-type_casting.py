# STRINGS can use single or double qoutes
my_string = 'Hello World'
my_string2 = "Hello World"
# NUMBERS
my_num = 4
# Booleans
my_bool = True
my_bool2 = False

# Check a variable's type
# 1. `type()` returns the CLASS of the variable it belongs to
print(type(my_string)) # <class 'str'> ; `str` is a built-in class
print(type(my_string) == str) # True

print(type(30)) # <class 'int'>
print(type(30.1)) # <class 'float'>

print(type(False)) # <class 'bool'>

# 2. Check using `isinstance()`
print(isinstance(my_string, str)) # True

# Type casting
print(type(20)) # <class 'int'>
print(type(str(20))) # <class 'str'>
print(type(int('20'))) # <class 'int'>
# NOTE: if you try to cast invalid values, it will give runtime error