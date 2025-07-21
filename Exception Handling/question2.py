# Write a Python program to demonstrate handling multiple exceptions.

try :
    num1 = int(input("Enter Divisor : "))
    num2 = int(input("Enter Divident : "))
    ans = num1 / num2
except ZeroDivisionError : 
    print ("Please do not enter zero as Divisor")
except ValueError :
    print ("invalid input")
else :
    print ("The answer is : ", ans)
finally :
    print ("Finally block executed")