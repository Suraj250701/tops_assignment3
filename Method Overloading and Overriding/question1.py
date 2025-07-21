# Write Python programs to demonstrate method overloading and method overriding. 
# overriding :
class First:
    def Func(self):
        print ("First class")
class Second(First):
    def Func(self):
        print ("Second class")
objSecond = Second()
objSecond.Func()



# opreator overloading example:
class Division:
    def __init__(self,x):
        self.x = x
    def __add__(self,other):
        return self.x / other.x
a = Division(36)
b = Division(6)
print (a + b)