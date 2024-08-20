# Object Oriented Programming is a paradigm (Method) which involves classes and objects.
# Class: Blue print for an object.
# Object: Instance of a class.
# Demonstration:
class myClass:
    print("Greetings from myClass")
    pass

myClass()

# There are three methods involved when dealing with OOPS.
# 1. Class creation:
class sampleClass:
    print("Greetings from sampleClass")
# 2. Instantiation:
sampleClass()
# 3. Object creation:
sampleClassInstance = sampleClass()
sampleClassInstance

# Constructor:
# A constructor is executed at the time of object creation. 
# A certain naming convention is followed to identify a constructor method in a class.
# Demonstration:
class constructorDemo:
    def __init__(self) -> None:
        pass
# Note: In the '__init__' method, the parameter 'self' is the class itself.