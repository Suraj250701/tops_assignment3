# Write a Python program to open a file in write mode, write some text, and then close it.
def usr_file_demo():
    file = open(".\\Opening and Closing Files\\question1.txt", "w")
    file.write(input("Enter text to write to the file: "))
    file.close()

usr_file_demo()