# Set is a sequence that stores unique elements only.
# Declaration:
my_set = {1, 2, 3, 4, 5, 5}
# It prints {1, 2, 3, 4, 5} and skips 5 as it is already present.
print(my_set)

# Just like in mathematics, python supports various operations that can be performed on two sets.
my_set1 = {1, 2, 3, 4, 5, 6}
my_set2 = {5, 6, 7, 8, 9, 10}
# 1. Union:
print(my_set1.union(my_set2))
# or
print(my_set1 | my_set2)
# 2. Intersection: 
print(my_set1.intersection(my_set2))
# or
print(my_set1 & my_set2)
# 3. Difference:
print(my_set1 - my_set2)
# or
print(my_set1.difference(my_set2))
# 4. Symmetric difference:
print(my_set1.symmetric_difference(my_set2))
# or
print(my_set1 ^ my_set2)

# Note: Set contains unordered elements, thus cannot be accessed by their index numbers
# The following line of code returns type error saying that 'sets are not subscriptable'.
print(my_set[0])