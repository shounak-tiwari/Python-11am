# chr 
# ord

ascii_by = {}
for x in range(65,91):
    ascii_by[x] = chr(x)


ascii_by[65]= 'W'

print(ascii_by)
text = "PALAK"


text = text.translate(ascii_by)

print(text)