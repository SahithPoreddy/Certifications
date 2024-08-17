# Kwargs or Keyword arguments is more or less like 'args' except that they contain keyword arguments.
# Demonstration:
def kwargsDemo(**kwargs):
    sum = 0
    for k, v in kwargs.items():
        sum += v
    return sum

print(kwargsDemo(Coffee = 2, Tea = 5, Latte = 10))