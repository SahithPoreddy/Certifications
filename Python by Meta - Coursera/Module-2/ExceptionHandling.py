# Mistakes are invetible while writing code. Syntax errors are the errors caused by the programmer and in most cases can be resolved with the help of the IDE.
# But there are few exceptions with the input or operation that need to be handled. This process is called exception handling.
# Demonstration:
def division(num1, num2):
    try:
        return num1 / num2
    except Exception as e:
        return e

# Prints '2'    
print(division(4, 2))
# Prints 'Divison by zero' error.
print(division(4, 0))

# In exception handling, multiple except statements can be chained to make specialized error as well as generic error.
# Demonstration:
def div(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError as e:
        return e
    except Exception as e:
        return e
    
# Prints '5'
print(div(10, 2))
# Prints 'Divison by zero' error.
print(div(10, 0))