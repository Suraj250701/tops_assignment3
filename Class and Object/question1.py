# Write a Python program to create a class and access its properties using an object.

class Greeting: 
    def __init__(self,name):
        self.name = name
    def display(self):
        print (f"Hello there, my name is {self.name}")        
objparth = Greeting("Suraj")
objparth.display()