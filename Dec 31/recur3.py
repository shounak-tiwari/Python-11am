#reverse string using recursion

def reverse(string ,n):
	if n==0:
		return ""
	return string[n-1]+reverse(string,n-1)


x= reverse("Anjali",len("Anjali"))

print(x)