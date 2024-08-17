# Dictionary is a collection of key-value pairs.
# Declaration:
my_dictionary = {1: "One", 2: "Two"}
print(type(my_dictionary))
# The value can be accessed through the key.
print(my_dictionary[1])
# The value of a key can be changed by assigning a different value.
my_dictionary[1] = "Not one"
print(my_dictionary)
# Note: Keys are not repeated in dictionaries. If a key-value pair is added to the dictionary in which the key already exists, the older key-value pair is override with the new pair.
# The following overrides the existing key-value pair.
my_dict = {1: "One", 2: "Two", 1: "Not one"}
print(my_dict)