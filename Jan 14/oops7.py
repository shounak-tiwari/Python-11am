# Write a Python program to demonstrate multiple inheritance where a class inherits from two base classes.

class Login:
    def __init__(self):
        self.username = input('Enter user name : ')
        self.password = input('password : ')
    
    def responsePage(self):
        if self.username and self.password:
            print(f"welcome {self.username}")

class registrations:
    def __init__(self):
        username  = ""
        password = ""
        firstname = ""
        lastname = ""

        if username and password and firstname and lastname:
            print("registration success ful")
    
        else:
            print('enter correct details ')

    

class derived(Login,registrations):
    def __init__(self,x):
        if x == 1:
            Login.__init__(self)
            Login.responsePage(self)
        else:
            registrations.__init__(self)
        
    
student = derived(1)



