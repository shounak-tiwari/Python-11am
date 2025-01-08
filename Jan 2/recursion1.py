# Write a Python program to calculate the sum of a list of numbers using recursion.
def Add(num,size):
    if size==0:
        return num[size]
    return num[size]+ Add(num,size-1)

number = [1,2,3,4,5,6,7,8,9,10]

print(Add(number,len(number)-1))