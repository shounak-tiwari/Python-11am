n = int(input("Enter nth term : "))
for no in range(n):
    flag = 0
    for x in range(2,no):
        if no %x==0:
            flag=1
            break

    if flag ==1 :
        print("not prime ",no)
    else:
        print("prime",no)