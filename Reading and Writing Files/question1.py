# Write a Python program to read the contents of a file and print them on the console.
with open(".\\Reading and Writing Files\\quesion1.txt", "a") as file:
    content = file.write(input("Enter a string to write into the file: "))
    
with open(".\\Reading and Writing Files\\quesion1.txt", "r") as file:
    print("File Contains : ", file.read())