def add(n:int):
	if n ==0:
		return 0
	return n + add(n-1)


x = add(5)
print(x)