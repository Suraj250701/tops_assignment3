# Write a Python program to handle exceptions in a simple calculator (division by zero, invalid input).

try :
    num1 = int(input("Enter Divisor : "))
    num2 = int(input("Enter Divident : "))
    ans = num1 / num2
except ZeroDivisionError :
    print ("Please do not enter zero as Divisor")