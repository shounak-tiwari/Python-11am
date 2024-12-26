D = dict()
while True:
    # declare key 
    key = str(input('Enter the key : '))
    if key =="" or key ==" ":
        break
    value = str(input('Enter the value : '))
    D[key] = value

print(D)