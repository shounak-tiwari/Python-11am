student ={
    1:{'Name':'Anjali verma','Contact':'7440244470','E-mail':'anjaliverma0409@gmail.com'},    2:{'Name':'Disha','Contact':'8889485940','E-mail':'disha@gmail.com'},8:{'Name':'Palak','Contact':'7023512492','E-mail':'python@gmail.com'},
    4:{'Name':'Anjali','Contact':'8120597499','E-mail':'anjali@gmail.com'},    5:{'Name':'Pushkar','Contact':'7597025147','E-mail':'pushakar@gmail.com'},}

choice = int(input('enter the id '))
x = list(filter(lambda x: x==choice,student))

for i in x:
    print(student[i])
