# for loops are used for iterating over sequences like tuples ,
# list,strings , and ranges 
# a. for loops can iterarete over any iterable object
# b. not able to manually manage the index
# c. For loops allows you to apply the same operation to every items 
# within the loops 

students = [
    "Aarav",
    "Riya",
    "Rahul",
    "Neha",
    "Karan",
    "Pooja",
    "Amit",
    "Sneha",
    "Vikram",
    "Anjali"
]
flag = False
name =str(input("Enter the name of student : "))
name = name.capitalize()
for x in students:
  if x == name:
    print("Student found in list ")
    break
  if x == students[-1]:
    flag = True
if flag:
  print("Student not found in list")
