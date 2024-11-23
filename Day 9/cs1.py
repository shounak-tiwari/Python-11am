from re import match
email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
name_regex = r"^[A-Za-z]+(?:[' -][A-Za-z]+)*$"
phone_number =  r"^(?:\+91|91)?[6-9]\d{9}$"
date_of_birth_regex = r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19|20)\d{2}$"
first = input("Enter the first name : ")
if match(name_regex,first):
    print("First name is valid ")
    last = input("Enter the last name : ")
    if match(name_regex,last):
        print("last name is valid ")
        email = input(f'Enter the email of {first} {last} : ')
        if match(email_regex,email):
            print("email is valid ")
        else:
            print("email is not valid ")
    else:
        print("last name is not valid ")
else:
    print("First name is not valid ")