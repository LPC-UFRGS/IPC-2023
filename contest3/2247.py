caso = 0
while(True):
    n = int(input())
    if n==0:
        break

    caso+=1
    print(f'Teste {caso}')
    

    joao = 0
    ze = 0
    for i in range(n):
        a, b = input().split()
        joao+=int(a)
        ze+=int(b)
        print(joao-ze)
    print()