import re

pattern_name = r"^[A-Za-z]+(?:[' -][A-Za-z]+)*$"


pattern_email =  r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"



# first = input("enter the first name of student : ")
# last = input("enter the last name of student : ")




# if len(first) <=8 and re.match(pattern_name,first):
#     print("first name is valid ")
#     if len(last)<=8 and re.match(pattern_name,last):
#         print("last name is valid ")
#     else:
#         print("please enter valid last name ")
# else :
#     print("please enter valid name")


email = input('Enter the email : ')

if re.match(pattern_email,email):
    print('yes !valid ')

else:
    print("Not valid ")