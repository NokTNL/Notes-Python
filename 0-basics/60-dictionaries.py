# DICTIONARIES hold key-value pairs, looks very much like Javascript plain objects
# It's declared with `{}`
# Both strings and numbers can be keys
my_dict = {1 : 'one', 'two' : 2}
# Accessing dictionary values: use `[]`
print(my_dict['two']) # '2'
# Inlining access works as well:
print({1: 'ONE'}[1]) # 'ONE'