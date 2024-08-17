# Variable scope refers to from where a variable can be accessed.
# There are essentially four types for variable access. They can be remembered by the 'LEGB' abbreviation with 'B' being the superset of all.
# L -> Local scope
# E -> Enclosed scope
# G -> Global scope
# B -> Built-in scope

# Local scope:
# The variables declared are accessed only within the function in which they are defined in.
# Demonstration:
def localScope():
    local_variable = 5
    print(local_variable)

localScope()

# Enclosed scope:
# Enclosed scope is defined by the nested functions. It means that the variables defined in the inner function are not accessible by the members of the outer/parent function.
# Demonstration:
def outerFunction():
    outer_variable = 5
    def innerFunction():
        inner_variable = 10
        # The following two lines of code will run without any error as it has access to the superset variables.
        print(outer_variable)
        print(inner_variable)
    # Note: innerFunction() is to be called explicitly within the outer function in order to execute it.
    innerFunction()
    # The following line of code returns an error 'inner_variable' is not defined.
    # print(inner_variable)

outerFunction()

# Global scope:
# Global scope implies that the variables that can be accessed by any function within the same file.
global_variable = 10

def globalScope():
    print(global_variable)
    def innerGlobal():
        print(global_variable)
    innerGlobal()

globalScope()

# Built-in scope:
# Built-in scope is nothing but the reserved keywords like 'for', 'in', 'while' etc...