# Everything in Python is an object, even for primitive values like numbers and strings.
# That means they can hav attributes and methods (accessed with the . notation)

#
# Classes
#
class Human:
    # All methods (incl. constructor) MUST receive `self` as the first parameter, which points to the object instance itself.
    # And then the remaining parameters are what the user can call
    def speak(self, speech = "Hi"):
        print(speech)

    # Constructor
    def __init__(self, name):
        self.name = name # It just assigns to the object like this without defining the field / shape in advance

tom = Human("Tom")
tom.speak() # Hi
tom.speak("Hey!") # Hey

#
# Inheritance
#
class Teacher(Human):
    def speak(self, speech):
        Human.speak(self, speech) # Just call inherited methods like this
        print("What is your question, my pupil?")

mr_Jones = Teacher("Mr. Jones")
mr_Jones.speak("Now turn to page 309.")
# A class can inherit multiple base classes. When looking for inherited attributes / methods, the base classes will be searched from left to right.