## User inputs
# `input()` will wait for user's input in the command line and pause the code's execution. It returns a string. 
user_input = input("Give me something:\n")
print(user_input)

# DICTIONARIES are like Javascript objects or maps, holding key-value pairs
# It's declared with `{}`
# Both strings and numbers can be keys
my_dict = {1 : 'one', 'two' : 2}
# Accessing dictionary values: use `[]`
print(my_dict['two']) # '2'
# Inlining access works as well:
print({1: 'ONE'}[1]) # 'ONE'