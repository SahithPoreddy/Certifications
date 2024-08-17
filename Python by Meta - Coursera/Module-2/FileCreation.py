# Files can be created with the mode = 'w'. If the specified file does not exist, it will create a new file or if the file already exists, it will override the contents of the file.
# Demonstration:
with open('./Module-2/Test/New.txt', 'w') as file:
    file.writelines(['First line', '\nSecond line'])