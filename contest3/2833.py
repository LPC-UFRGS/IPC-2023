def simulate(v, obj):
    nl = []
    for i in range(0, len(v), 2):
        if (v[i] in obj and v[i+1] in obj):
            return []
        elif v[i] in obj:
            nl.append(v[i])
        elif v[i+1] in obj:
            nl.append(v[i+1])
        else:
            nl.append(0)
    return nl
v = input().split()
obj = ['1', '9'] 
round = 0
while len(v)!=0:
    v = simulate(v, obj)
    round+=1
placar = ['oitavas', 'quartas', 'semifinal', 'final']
print(placar[round-1])