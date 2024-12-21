from math import fabs 
x = 73
y =19

print('before')
print(x,y)

x = x^y

y = x^y # 30 ^ 20-> 10

x = x^y # 30 ^ 10 ->20

print('after')
print(int(fabs(x)),int(fabs(y)))