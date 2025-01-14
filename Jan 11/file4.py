import datetime
file =  open("StudentsRecord.txt","a")

for x in range(1,8):
	Name = input("Enter the name of students : ")
	CurrentInputTime = str(datetime.date.today())

	file.write(Name)
	file.write(CurrentInputTime)
	file.write("\n")

