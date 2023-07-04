# Strings concantenation can be done with +
my_string = "AHAHAHAHAH"
print("Hello World " + my_string + "!")
# NOTE: You CAN'T concat NUMBERS to strings using `+`

# Alternatively, use f-strings (similar to Javascript template literals)
# placeholders are inside `{}`
# NOTE: In f-strings you can use NUMBERS and it will be converted to a string for you
my_num = 25
print(f"I'm {my_num} years old!")