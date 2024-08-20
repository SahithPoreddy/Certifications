# Comprehension is the process of generating a new sequence from the existing sequence.
# This allows the derived sequence to be in the desired format.
# There are four ways in comprehension:

# 1. List comprehension: Deriving a list from the existing list.
# Syntax = [<expression> for <variable> in <sequence> if <condition>]
data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_comprehension = [x for x in data1 if x % 2 == 0]
print(*list_comprehension)

# 2. Dictionary comprehension: Deriving a dictionary from the existing list.
# Syntax = {key : value for key, value in <sequence> if <condition>}
# Note: One or two lists can be used.
# Example for one list:
data2 = [1, 2, 3, 4, 5]
dictionary_comprehension = {x : x * 2 for x in data2}
print(dictionary_comprehension)
# Example for two lists:
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
months_and_numbers = {key : value for (key, value) in zip(number, months)}
print(months_and_numbers)

# 3. Set comprehension: Deriving set from the existing list.
# Syntax = {<expression> for <variable> in <sequence> if <condition>}
# Demonstration:
data3 = [1, 2, 3, 4, 5]
set_comprehension = {x for x in data3 if x not in [4, 5]}
print(set_comprehension)

# 4. Generator comprehension: It is more like set comprehension except that parenthesis are used instead of curly braces.
# Note: The elements cannot be accessed directly in a generator comprehension.
data4 = [1, 2, 3, 4, 5]
generator_comprehension = (x for x in data4 if x not in [3, 4, 5])
print(*generator_comprehension)