# Lists are dynamic arrays in python.
# Lists can store elements of any data type and also stores lists as an element i.e. nested lists.
# It is also possible to store elements of different data types to be stored under the same list.

# Creation of a list:
list1  = [1, 2, 3, 4, 5]
# Lists can be printed out in three ways:
# 1. Using *<list_name>:
print(*list1)
# 2. Direct method:
print(list1)
# 3. Using a loop:
for i in list1:
    print(i, end = ',')
print()

# Updating a list:
# There are three ways available to update a list:
# 1. During creation:
list2 = [1, 2, 3, 4, 5]
# 2. Using 'insert' method:
# 'insert' method is used to insert an element at an index.
list2.insert(len(list2), 6)
# 3. Using 'append' method:
# 'append' method is used to insert an element at the end of the list.
list2.append(7)
# 4. Using 'extend' method:
# 'extend' method is used to insert another list of elements to the current list.
list2.extend([8, 9, 10])

print(*list2)

# Removing elements from the list:
# There are two ways to remove an element from a list:
# 1. Using 'pop' method:
# 'pop' takes in the index of the element to be deleted as an paramter.
list2.pop()
# 2. Using 'del' keyword:
del list2[8]
print(*list2)