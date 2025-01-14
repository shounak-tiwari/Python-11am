class student:
    # methods inside the class 

    def methodOfClass(self):
        name = input("Enter the name :  ")
        self.deesha= name 
    
    def display(self):
        print('name of student : ',self.deesha)
    
object = student()

object.methodOfClass()


# in python, user not able to call feild of methods with class object this method's feild can not callable from outside of methods 