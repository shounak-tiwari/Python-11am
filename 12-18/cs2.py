#  if elif else control statement : when single condition is true all conditions terminate

# write a program to check year is leap or not 
year = int(input("Enter the year  : "))

if year % 4 ==0 and year%100 !=0:
    print("year is leap")
elif year%400==0:
    print("year is leap")
else:
    print("not leap")