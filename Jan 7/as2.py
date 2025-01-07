import functools

lst = [1,2,3,4,5]

x = functools.reduce(lambda x,y:x*y,lst)

print('The reduce of this function : ',x)