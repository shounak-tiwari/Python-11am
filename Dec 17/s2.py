s1= {1,2,3,4}
s2 = {1,2,5,6,7,8}

print(f'value of s1: {s1} and s2: {s2} ')

# operators in a set => set -> list -> list -> set  (+,*, - )

diff = s1-s2
print(f'difference between s1 and s2 : {diff}') 


diff = s1.difference(s2)
print(f'difference between s1 and s2 : {diff}') 

s1 = {10,20,30,40}
s2 = {50,20,30,40}

result = s1.symmetric_difference(s2)
print('symmetric difference : ',result)