# Just like any other programming language, python has the ability to take the input and produce ouput through 'input()' and 'print()' functions.
# 'input()' function initiates the input from the terminal.
# 'print()' function prints any data type value to the terminal.

# 'input()' demonstration.
var_input = input('Please enter your name : ')
print(var_input)
# Note: The message parameter is optional in the input function.
# Note: By default, all the input type is 'str'. However, it can be converted to desired data type through type casting.
var_str = input('Enter a number : ')
print(type(var_str))

# 'print()' demonstration.
print('Hello there')
# It allows all the arithmetic operations directly as a paramter to the function.
print(3 + 4)
# 'print()' function also allows string concatenation.
print('Hello ' + var_input)
# 'print()' function prints comma separeted values as well.
print(1, 2, 3, 4, 5)
# 'print()' has an option functional paramter 'sep' which separates two values in the print function.
print('Hello', 'There', sep = ',') 
# Formating allows changes to be made in the print function.
print('My name is {} and I am {} years old'.format('Sahith Chandra', '21'))
print('I like {0} more than {1}'.format('Bananas', 'Oranges'))