# Polymorphisms : Poly : many morphisms : forms 
# single entity performs many different forms , according to situations 
'''
Polymorphisms : 
1. Compile time poly
    1. function overloading 
    2. operators overloading 
2. Run time poly 
    1. Method overriding 
'''
class A:
    def show(self):
        print("this is base class")

class B(A):
    def show(self):
        print("The is Universal informatics")

    
A_obj = B()
A_obj.show()