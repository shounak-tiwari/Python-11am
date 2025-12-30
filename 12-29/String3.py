# String is immutable means not change after assign 
name = "Sneha"
name = "A" + name[1:]
print(f"After change the value of index zero {name}")
del name 
print(name)