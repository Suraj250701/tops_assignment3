# Write a Python program to read a string, an integer, and a float from the keyboard and display them.

def usr_input():
    string_input = input("Enter a string: ")
    int_input = int(input("Enter an integer: "))
    float_input = float(input("Enter a float: "))

    print("String:", string_input)
    print("Integer:", int_input)
    print("Float:", float_input)

usr_input()