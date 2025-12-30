import re

Digit_sample_reGex = r"^\d{10}+$"
contact = input("Enter the contact number : ")

if re.match(Digit_sample_reGex,contact):
    print("valid contact number")
else:
    print("Invalid contact number ")