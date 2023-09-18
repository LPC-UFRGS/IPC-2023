n = int(input())
for _ in range(n):
    m = int(input())
    notas = input().split()
    notas_int = []
    for nota in notas:
        notas_int.append(int(nota))

    ordenados = sorted(notas_int, reverse=True)
    nao_trocou = 0
    for i in range(len(notas_int)):
        if notas_int[i] == ordenados[i]:
            nao_trocou += 1

    print(nao_trocou)
