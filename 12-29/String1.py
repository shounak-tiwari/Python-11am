# regEx = r"^[A-Za-z]+$" (Only letters) e.g. snehapatel
# regEx = r"^[A-Z][a-z]+$" Only letters e.g. Snehapatel
import re

Sample_Regular_expression = r"^[A-Z][a-z]+ [A-Z][a-z]+$"
Name = str(input("Enter the name of student "))
if re.match(Sample_Regular_expression,Name):
    print("Name is matched")
else:
    print("Name is invalid")