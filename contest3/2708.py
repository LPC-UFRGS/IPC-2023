pessoas = 0
jipes = 0
while True:
    s = input()
    if s=='ABEND':
        break
    a, b = s.split()
    b = int(b)
    if a=='SALIDA':
        pessoas+=b
        jipes+=1
    else:
        pessoas-=b
        jipes-=1
print(pessoas)
print(jipes)