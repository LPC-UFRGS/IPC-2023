v = int(input())
a = int(input())

parcela = v//a
resto = v%a
for i in range(a):
    v = parcela
    if resto>0:
        v+=1
        resto-=1
    print(v)