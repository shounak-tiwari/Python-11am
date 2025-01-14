name = input("Enter the file name : ")

file = open(f'{name}.xlsx')

if file:
	print("yes")
else:
	print("no")
# x = file.readline()

