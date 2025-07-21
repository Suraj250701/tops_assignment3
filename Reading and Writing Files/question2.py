# Write a Python program to write multiple strings into a file.
with open(".\\Reading and Writing Files\\question2.txt", "a") as file:
    string = input("Enter a string to write multiple strings into the file : ")
    file.write(string + "\n")