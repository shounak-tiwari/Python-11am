'''
String methods  for case conversions
1. len() : it is use for calculate length of string 
2. upper() : it is use for convert string into upper case 
3. lower() : it is use for convert string into lower case 
4. strip() : it is use for removing unwanted spaced in a  string 
5. capitalize() : it is use for convert first letter of string 
6. title(): it convert fist letter of each word in upper case 
7. swap case() : upper case <-> lowercase   
'''
s = "sneha patel"
print(f"The original string : {s}")

print(f"Total ELement in string {len(s)}")

s = s.capitalize()
print(f"String After capitalize : {s}")


s = s.upper()
print(f"String in  upper case : ")