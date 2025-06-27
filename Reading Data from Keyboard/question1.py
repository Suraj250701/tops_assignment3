# Write a Python program to read a name and age from the user and print a formatted output.

def usr_input():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    print("Name : {} & Age : {}.".format(name, age))
    print(f"Name : {name} & Age : {age}.")
usr_input()