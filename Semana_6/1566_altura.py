nc = int(input())
for _ in range(nc):
    _ = input()
    alturas = input().split()
    alturas = [int(altura) for altura in alturas]
    print(*sorted(alturas))
