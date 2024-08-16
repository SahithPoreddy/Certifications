# Functions are blocks of code used to perform a certain action upon calling
# A function/method may or may not take parameters as input and may or may not return a value.
# 'def' keyword is used to define a function in python

# Function with no parameters and return value
def say_hello():
    print("Hello there")

say_hello()

# Function with parameters and return value
def sum(a, b):
    return a + b

addition = sum(2, 3)
print(addition)