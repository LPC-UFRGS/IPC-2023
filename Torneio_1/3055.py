a = int(input()) #registro da nota 1
m = int(input()) #registro da media das notas


'''
(nota1 + nota2)/2 = media
nota1 + nota2 = 2*media
nota2 = 2*media - nota1
'''

b = 2*m - a #nota faltante

print(b)
