# Control flow determines how the program should be carried out.
# Condition and loops are two concepts used for control flow in programming.

# Condition:
# if, elif (else if), else is a condition based execution syntax.
if(3 > 2):
    print("It is greater")
elif(3 == 2):
    print("It is same")
else:
    print("It is smaller")
# An alternate and better solution for multiple conditions is a 'match'. A match essentially is a switch case for python.
# 'match' demonstration:
http_code = 200
match http_code:
    case 200 :
        print("Success")
    case 400:
        print("Bad request")
    case 500:
        print("Internal server error")
    case _:
        print("Unknown error")

# Loops:
# For loop and while are used to execute a task for certain number of times.
# 'for' loop:
for i in range(10):
    print(i)
# Certain parameters are used in the 'for' loop to add more functionality.
# break, continue, pass are the keywords used to complelty stop the loop, skip the next steps of the loop and ignore the conditions.
# 'break':
for i in range(10):
    print(i)
    if(i == 5):
        break
# 'continue':
for i in range(10):
    if(i == 5):
        continue
    print(i)
# 'pass':
for i in range(10):
    if(i == 5):
        pass
    print(i)
# 'while' loop:
# A while loop is executed until a condition is met.
var_temp = 0

while var_temp < 5:
    print(var_temp)
    var_temp += 1

# Nested loops are loops inside loops.
# Nested loops demonstration:
# Outer loop
for i in range(10):
    # Inner loop
    for j in range(10):
        print('0', end = " ")
    print()