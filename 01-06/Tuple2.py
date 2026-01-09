#create a tuple and enter the value and print total number of counts of that value in tuples

T1 = (1,1,4,3,2,1,7,5,2,1,1,1,1,4,3,2,1,7,5,2,1,1,4,3,2,1,7,5,2)
val = int(input("Enter the values "))
count = 0 
for x in T1:
    if x==val:
        count+=1
print("Total number of count in given tuples is : ",count)