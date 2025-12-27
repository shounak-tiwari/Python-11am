from re import match
sample = r"^[A-Za-z]{2,8}$"
name = str(input("enter the name of student : "))
if match(sample,name):
    print("valid input name ")
else:
    print("invalid input name")