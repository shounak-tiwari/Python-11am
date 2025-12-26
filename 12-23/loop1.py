x = 121

orginial = x 
rev = 0

while x!=0:
	ld = x%10
	rev = (rev*10)+ld
	x = x//10


if (rev != orginial):
	print("Not palindrom")

else:
	print("palindrom")