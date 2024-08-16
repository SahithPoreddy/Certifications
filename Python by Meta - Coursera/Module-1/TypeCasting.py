# Type casting is the process of converting the data type of a variable
# There are two kinds of type casting: 1. Implicit type casting 2. Explicit type casting
# Implicit type casting is taken care by the compiler, when the variable declared picks up the values larger than it is supposed to be.
# Note: Few type casting are not allowed in implicit type casting. For example, int -> str is not allowed.
# Explicit type casting, as the name suggests is explicitly converted by the programmer using built-in functions.

# Implicit type casting demonstartion
var_int = 5
print(type(var_int))
var_int = 5.5
print(type(var_int))

# Explicit type casting
var_float = 5.5
type_str = str(var_float)
print(type(type_str))