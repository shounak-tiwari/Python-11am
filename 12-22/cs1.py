# match statement in python is use for parttens of questions which is adding in python 3.10+version only it is depend upon Expression & case, those case is matched with expression  the expression case getting execute

num1 = int(input("Enter the number-1  : "))
operators = str(input("Enter the operators (+,-,/,*) : "))
num2 = int(input("Enter the number-2  : "))
match operators:
    case '+':
        print("the sum of number 1 and number 2 : ",num1+num2)
    case '-':
        print("The substraction of number 1 and number 2 : ",num1-num2)
    case '*':
        print("The multiplication of number 1 and number 2 : ",num1*num2)