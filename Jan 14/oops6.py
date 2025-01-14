# Write a Python program to demonstrate single inheritance by creating a Dog class that inherits from an Animal class.

class Animal():
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "bhow bhow bhow bhow" 


obj = Dog()
print(obj.sound())