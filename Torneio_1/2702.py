#ca, ba, pa =  [int(i) for i in input().split()] 

ca, ba, pa = input().split() # registra quantidades disponiveis

ca = int(ca)
ba = int(ba)
pa = int(pa)

cr, br, pr = input().split() # registra quantidades solicitadas

cr = int(cr)
br = int(br)
pr = int(pr)

soma = 0 #inicializa soma como 0

# para cada alimento, se a demanda for maior que a quantidade
# soma para o resultado a diferena entre demanda e quantidade

if cr>ca:
    soma = soma + (cr-ca)

if br>ba:
    soma = soma + (br-ba)

if pr>pa:
    soma = soma + (pr-pa)

print(soma)
