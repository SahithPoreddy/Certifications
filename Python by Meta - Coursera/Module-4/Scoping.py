# Scope refers to the availability of an attribute in the code base.
# LEGB (Local, Enclosed, Global and Built-in)
# In python, declared varibles are not global by default. However, scope of a varible can be manipulated using 'nonlocal' and 'global' keywords.

# 1. 'nonlocal':
def nonLocalDemo():
    non_local_var = 5
    print("The value of non local variable in the outer method before execution of inner method : ", non_local_var)
    def innerFunction():
        nonlocal non_local_var
        non_local_var = 10
        print("The value of non local variable in the inner method during execution : ", non_local_var)

    innerFunction()
    print("The value of non local variable in the outer method after the execution of inner method : ", non_local_var)

nonLocalDemo()

# 2. 'global':

def globalDemo():
    global global_var
    global_var = 5
    print("Value of global variable inside the method : ", global_var)

globalDemo()
print("Value of global variable outside the method : ", global_var)