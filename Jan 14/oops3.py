# constructor in python :
# default constructor 
# paramerize constructor 
# copy constructor 

# default constructor 
class Student:
    def __init__(self):
        self.name = input('Enter the name of student : ')
        self.age = float(input('Enter the age of student : '))
        self.contact = int(input('Enter the contact of student : '))
        self.email = input('Enter the email of student : ')

    
    def show(self):
        print("The name of student  : ",self.name)
        print("The age of student : ",self.age)
        print("The contact of student  : ",self.contact)
        print("The email of student : ",self.email)


obj = Student()
obj.show()