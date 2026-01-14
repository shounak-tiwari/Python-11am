# CONSTRUCTION : create memory when object is initlize with class , call automatically when object is init (init)
# DESTRUCTOR : distroy memory when object is completed 

class Employee:
    def __init__(self):
        print(id(self))
        self.nameEmployee = str(input("Enter the name of employee : "))
        self.salary = float(input("Enter the salary of employee : "))
        self.city = str(input("Enter the city of employee : "))
    def output(self):
        print("the name of employee : ",self.nameEmployee)
        print("the salary of employee : ",self.salary)
        print("the city of employee : ",self.city)
    
obj_1 = Employee()
print(id(obj_1))
obj_1.output()
