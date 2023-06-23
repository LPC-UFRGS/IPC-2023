m = int(input()) #registro idade dona monica
a = int(input()) #registro idade do filho 1
b = int(input()) #registro idade do filho 2

c = m - a - b    #idade do filho 3

idade_maior = 0 #inicializo variavel

if a>=b and a>=c:
    idade_maior = a
elif b>=a and b>=c:
    idade_maior = b
else:
    idade_maior = c

print(idade_maior)
