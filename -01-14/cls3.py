# Inheritance and abstractions 
# Inheritance : Interit it means reusebillity of code 
# reuse the properies of parent into child thats called inheritance  
class Models:
    def __init__(self):
        self.ModelName = str(input("Enter the model name of car : "))
        self.ModelNumber = str(input("Enter the model number of car : "))
        self.Price = float(input("Enter the price : "))
    def output(self):
        print("The model name of car  : ",self.ModelName)
        print("The model number of car : ",self.ModelNumber)
        print("The price of car : ",self.Price)
class CarDetails(Models):
    def __init__(self):
        Models.__init__(self)
        self.color = str(input("enter the color of car : "))
        self.seat_capacity = int(input("enter total seats : "))
    def output(self):
        Models.output(self)
        print("The color of car : ",self.color)
        print("The seating capacity of car  : ",self.seat_capacity)
mahindra_1 = CarDetails()
mahindra_1.output()