n = int(input())
t_on = 0
t_last = 0
t_atual = -1
for i in range(n):
    tempo_pessoa = int(input())
    if tempo_pessoa<=t_atual:
        t_atual+=tempo_pessoa-t_last
        t_on+=tempo_pessoa-t_last
    else:
        t_atual=tempo_pessoa+10
        t_on+=10
    t_last = tempo_pessoa
print(t_on)