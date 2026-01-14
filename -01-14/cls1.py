# CLASS : blue print of program 
#  OBJECT : real entity of class 
# self : track your currently object (instance)
# function of class : inputdata , outputdata 
class Student:
    def intputdata(self):
        print(id(self))
        self.name = str(input("Enter the name of student  : "))
        self.subject = str(input("Enter the subject name : "))
    
    def outputdata(self):
        print(f"The name of student is  : {self.name}")
        print(f"The subject of student is : {self.subject}")
    
obj_1 = Student()
print(id(obj_1))
obj_1.intputdata()

# obj_2 = Student()
# obj_2.intputdata()

# obj_3 = Student()
# obj_3.intputdata()


# obj_2.outputdata()