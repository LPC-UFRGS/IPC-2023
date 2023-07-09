while True:
    n = int(input())
    if n == 0:
        break

    cartas = list(range(1, n+1))
    removidas = list()
    while len(cartas) > 1:
        topo = cartas.pop(0)
        removidas.append(topo)
        topo = cartas.pop(0)
        cartas.append(topo)

    removidas_string = list()
    for carta in removidas:
        removidas_string.append(str(carta))
    removidas = ", ".join(removidas_string)
    print(f"Discarded cards: {removidas}")
    print(f"Remaining card: {cartas[0]}")
