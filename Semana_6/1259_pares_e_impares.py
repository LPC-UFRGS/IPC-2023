n = int(input())
pares = []
impares = []
for _ in range(n):
    m = int(input())
    if m % 2 == 0:
        pares.append(m)
    else:
        impares.append(m)

pares = sorted(pares)
impares = sorted(impares, reverse=True)
lista = pares + impares
for num in lista:
    print(num)
