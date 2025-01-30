# To handle exceptions in Python:
myNum = 1
try:
    if myNum > 10:
        raise ValueError
    else:
        print(f"myNum is {myNum}")

except ValueError:
    print("myNum is bigger than 10!")

# Catch-all block
except: 
    pass # i.e. an empty block that does nothing
# Clean-up block
finally:
    myNum = 0

# Using the `with` statement can simplify this for a bit. For example this is how you should handle file I/O:
try:
    file = open('./new-file.txt', "w")
    file.write('Hi')
finally:
    file.close() # This needs to be called regardless, otherwise may cause bugs when trying to write the file again

# It can be simplified to this:
with open('./new-file.txt', "w") as file:
    file.write('Hi!')
print("The file was written successfully!") # This is only reacheable if no exceptions were thrown above
# To use `with`, the object created by the operation must have an __enter__ and __exit__ method defined
# - __enter__ creates and returns the resource you want to create (e.g. `file` in this case)
# - __exit__ handles the cleanup for you like the `finally` block (e.g. `file.close` in this case)