# write a python program for calculate gross salary of employee when basic salary of employee is entered via keyboards and his house rent is 3.5% and dearness allowance is 4.6% of  basic salary ?
basic_salary = float(input("Enter the Salary of employee : "))
house_rent = (3.5*basic_salary)/100
dearness_allowance = (4.6*basic_salary)/100
#now we calcualte gross ssalary gross_salary = basic_Salary + house_rent + dearness_allowance
gross_salary = basic_salary+house_rent + dearness_allowance
print(gross_salary)