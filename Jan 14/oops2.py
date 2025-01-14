# constructor or initlization methods 
# contstructor is methods which call automatically in python 
# it is a special methods which is use as a magic methods in python in python construtors is initization from object but it's name is different 

# class declared 

class Student:
    def __init__(self):
        print("welcome in constructor ")
    
    def __del__(self):
        print("this is distructor of class Student ")

studentObject =Student()


