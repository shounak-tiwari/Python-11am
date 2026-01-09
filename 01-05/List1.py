list1 = [1,2,6,3,4,5,6]
val = 6
k=0
for i in range(len(list1)):
    if(list1[i]!=val):
        list1[k] =list1[i]
        k+=1
del list1[k:]
print(list1)
