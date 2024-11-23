units = int(input("Enter the units : "))

if units<=30:
	payable_amount = units*334
	payable_amount = payable_amount /100
	subsidy = payable_amount -71
	payable_amount = payable_amount-subsidy
	print("Your Payable amount : ",payable_amount)


elif units<=50:
	payable_amount = units*427
	payable_amount = payable_amount /100
	subsidy = payable_amount -71
	payable_amount = payable_amount-subsidy
	print("Your Payable amount : ",payable_amount)
	

elif units<=150:
	payable_amount = units*530
	payable_amount = payable_amount /100
	subsidy = payable_amount -124
	payable_amount = payable_amount-subsidy
	print("Your Payable amount : ",payable_amount)
	

elif units<=300:
	payable_amount = units*661
	payable_amount = payable_amount /100
	subsidy = 27 *(units//100)
	payable_amount = payable_amount-subsidy
	print("Your Payable amount : ",payable_amount)
	
