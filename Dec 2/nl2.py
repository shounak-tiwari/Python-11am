
	# _	_	_	_	*	row = 1 , spc = 4 , star = 1
	# _	_	_	*	*	row = 2 , spc = 3 ,star = 2 
	# _	_	*	*	*	row = 3 , spc = 2 , star = 3
	# _	*	*	*	*	row = 4 , spc = 1 , star = 4
	# *	*	*	*	*	row = 5 , spc = 0 , star = 5 

# total no of rows - current row  = spc 
# 5 - 1 => 4
# 5 - 2 => 3


row = 5
col=5

# range => 1 => 5

for r in range(1,row+1):
	# 
	for space in range(1,row-r+1):
		print("_",end=" ")

	for c in range(1,r+1):
		print("*",end=" ")
	print("\n")