# Args allows 'n' number of arguments to be passed as the arguments to a function.
# Traditionally the number of variables to be passed should be matched with the number of arguments accepted by the function.
# But with the help of args, this problem is eliminated.
# Demonstration:
def argsDemo(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(argsDemo(1, 2, 3, 4))