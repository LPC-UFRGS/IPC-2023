n = int(input())
palavras = input().split()

for i in range(n):
    if len(palavras[i])==3:
        if palavras[i][:2]=='OB':
            palavras[i] = 'OBI'
        elif palavras[i][:2]=='UR':
            palavras[i] = 'URI'

print(*palavras)