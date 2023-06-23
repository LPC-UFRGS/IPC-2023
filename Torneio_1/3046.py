n = int(input()) #registra o n do duplo n

'''
vendo o padra apresentado na questao
percembemos que o numero de dominos cresce
de maneira linear, sempre de 1 em 1,
de maneira analoga a uma progressao aritmetica

por exemplo o domíno de grau N: terá
número do dominó | quantidade
0                | 1   
1                | 2
2                | 3
3                | 4
4                | 5
5                | 6
.                | 
.                | 
.                | 
n                | n+1

1+2+3+4+...+(n+1) = n*(n+1)/2
'''
n = n+1
soma = int(n*(n+1)/2) 
print(soma)
