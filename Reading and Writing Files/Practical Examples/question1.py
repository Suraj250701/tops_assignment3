# Write a Python program to create a file and print the string into the file.

def write_to_file():
    with open(".\\Reading and Writing Files\\Practical Examples\\quesion1.txt", "a") as file:
        content = file.write(input("Enter a string to write into the file: "))
    with open(".\\Reading and Writing Files\\Practical Examples\\quesion1.txt", "r") as file:
        print("File Contains : ", file.read())

write_to_file()