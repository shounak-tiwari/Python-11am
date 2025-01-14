# try , except , else , finally 
try:
    file  = open('student.txt') 

except FileNotFoundError as e :
    print(f'File is not found in given path :  {e}')



