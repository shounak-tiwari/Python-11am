# trimming and replacing 
name = "     sneha patel    "
print(len(name))
print(f"original name : {name}")

name = name.strip()# it removes all the space from both end of string 
print(len(name))
print(f"after apply strip function : {name}")

# lstrip()
# rstrip()

text = "Hello! Guest , Guest is came from usa ,Guest , Guest"

text = text.replace("Guest","sneha")

print(text)