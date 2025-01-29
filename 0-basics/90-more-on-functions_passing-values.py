#
# Passing values
#
# Everything in Python is an object.
# Whenever you assign one variable to another, or pass it as a parameter into a function, you pass a copy of the reference to that object.
# When you mutate the newly assigned variable, how it behaves depends on the mutability of the object
# - For immutable objects, a new object will be created if you do this. These includes numbers, strings and tuples
# - Everything else are mutable and you will modify the original thing
num1 = 1
num2 = num1
num2 += 1 # only num2 is affected
print(f"num1: {num1}, num2: {num2}") # num1: 1, num2: 2

list1 = ["A", "B"]
list2 = list1
list2.append("C")
print(f"list1: {list1}, list2: {list2}") # list1: ['A', 'B', 'C'], list2: ['A', 'B', 'C'] <-- both affected

def add_one(num):
    num += 1 # num has a NEW object assigned to it now
    print(f"Inside the function, num is {num}") # 11
num10 = 10
add_one(num10)
print(f"Outside the function, num is {num10}") # 10

#
# Scope
#
# Variables created has global scope, while functions create local scope for variables
myNum = 1
def myFunc():
    myNum = 2 # This is local to the function, and it overrides that of the global one
    print(f"Inside the function, myNum is {myNum}") # 2
myFunc()
print(f"Inside the function, myNum is {myNum}") # 1