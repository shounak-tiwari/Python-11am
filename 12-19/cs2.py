'''
if else nested control statement 
check eligiblity 
vits:
    qualification : 65% higher secondary examinations 
    ug : 60% higher examinations
    age : 17+
'''
age = int(input("Enter the age of candidate : "))

if age >17:
    qualification = float(input("Enter your higersec school examination score : "))
    if qualification>=60:
        ug = float(input("Enter the total percentage UG exam : "))
        if ug>= 60:
            print("yes you're eligible for test")
        else:
            print("Oops ! ug score is to low")
    else:
        print("Oops! higher sec exam marks is not matched ")
else:
    print("age not matched")