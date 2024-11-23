year = int(input("Enter the year : "))
if year % 400 ==0:
    print("leap ")
elif year % 4==0 and year %100!=0:
    print("leap")
else:
  print("not leap")