# first program of oops 
try: 
    class Student:
        def inputDetails(self):
            print("Hello This is my First program of oops ")
    # object 
    obj = Student()
    obj.inputDetails()
except NameError as e:
    print(e ,"Class name is not valid, please use valid class name ")