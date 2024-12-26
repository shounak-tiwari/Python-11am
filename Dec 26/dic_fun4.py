D = {'Name': 'universal', 'address': 'bhawarkua indore', 'contact': '7411111111'}

# get function return the value of given key 

x = D.get('contact')

print(x)


# return all items in a dict 

x = D.items()
print(x)

# return all keys in a dict

x = D.keys()
print(x)

# similar values function also work in dict 

x = D.values()
print(x)


# pop function remove that items whose key is given
D.pop('contact')

print(D)

# pop item function automatically remove last item of dict

D.popitem()
print(D)