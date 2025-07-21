# Write a Python program to read a file and print the data on the console.

def read_file():
    with open(".\\Reading and Writing Files\\Practical Examples\\quesion1.txt", "r") as file:
        print("File Contains : ", file.read())

read_file()