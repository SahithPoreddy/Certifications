# Reversing a string in python can be acheived by the extended slice operator.
# 1. Using extended slice operator:
original_str = 'Hello'
reversed_str = original_str[::-1]
print('Reversed string : ', reversed_str)

# 2. Using recursion:
def reverseString(str):
    if len(str) == 0:
        return str
    else:
        return str[1:] + str[0]
    
str1 = 'Tomato'
print(reverseString(str1))