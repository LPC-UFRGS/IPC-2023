a = int(input())
print(a)

b = int(a / 100)
print(b, "nota(s) de R$ 100,00")

a = a - (b * 100)
c = int(a / 50)
print(c, "nota(s) de R$ 50,00")

a = a - (c * 50)
d = int(a / 20)
print(d, "nota(s) de R$ 20,00")

a = a - (d * 20)
e = int(a / 10)
print(e, "nota(s) de R$ 10,00")

a = a - (e * 10)
f = int(a / 5)
print(f, "nota(s) de R$ 5,00")

a = a - (f * 5)
g = int(a / 2)
print(g, "nota(s) de R$ 2,00")

a = a - (g * 2)
h = int(a / 1)
print(h, "nota(s) de R$ 1,00")