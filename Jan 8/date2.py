import datetime
# use format specifiers 
x = datetime.datetime.now()
year = x.strftime("%d / %m / %Y")
print(f"year : {year}")