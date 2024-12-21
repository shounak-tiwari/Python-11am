# demo : enrollment = DX01
# demo : enrollment = DX02
# demo : enrollment = DX03
# demo : enrollment = DX04
# demo : enrollment = DX05
# demo : enrollment = DX06
Dic = dict()
for x in range(1,7):
    key = f"DX0{x}"
    name = input('enter the name : ')
    Dic[key] = name
# after dict creation printing 
print(Dic)
