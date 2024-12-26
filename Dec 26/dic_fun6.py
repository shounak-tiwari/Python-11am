D = {'Name': 'universal', 'address': 'bhawarkua indore', 'contact': '7411111111'}

user_choice = str(input('enter user choice (Name/address/contact): '))

x = D.get(user_choice)

print(x)