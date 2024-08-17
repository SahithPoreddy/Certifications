# Files are essential part of the programming. Python offers various methods through which files can be accessed in various modes.
# Read, Write, Append and Delete are the operations that can be performed on a file.
# Demonstration:
# In this case the file is to be close explicitly.
file = open('./Module-2/Test/Test.txt','r')
data = file.readline()
file.close()
print(data) 

# Another way through which we can automatically close the file and also have better file exception handling is through 'with' statement.
# Demonstration:
with open('./Module-2/Test/Test.txt', 'r') as file:
    data = file.readline()
    print(data)