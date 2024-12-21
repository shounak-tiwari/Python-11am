item_name = str(input('Enter the name of item : '))
price_ent = float(input(f'enter the price of {item_name} : '))

# result = 'The price of items : {price:.2f}'

# result = result.format(price = price_ent)

# print(result)

print('The price of items : {price:.2f}'.format(price = price_ent))
