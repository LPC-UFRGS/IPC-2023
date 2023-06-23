n = int(input())
p, c, q = input().split()

p = int(p)
q = int(q)

resultado = 0

if c == '+':
    resultado = p+q
else:
    resultado = p*q

if resultado > n:
    print("OVERFLOW")
else:
    print("OK")
