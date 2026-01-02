lst = []
# type function is use for checking type of refer... 
print(type(lst))
lst = ['Apple','Banana','Grapes','PineApple','logitech','Sneha']
print(lst)
# access element of list using index 
print(lst[0])
print(lst[1])
print(lst[len(lst)-1])
index = lst.index('logitech')
lst[index] = "Akash"
print(lst)