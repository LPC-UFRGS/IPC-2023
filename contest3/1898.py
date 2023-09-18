def getvalue(cpf, s1):
    value = ''
    exp = 0
    for i in s1:
        if i >= '0' and i<='9':
            if len(cpf)<11:
                cpf+=i
            else:
                value+=i
                if exp<0:
                    exp-=1
                if exp<-2:
                    break
        elif i == '.':
            value+=i
            exp=-1
    return cpf, value


cpf = ''
s1 = input()
s2 = input()
cpf, v1 = getvalue(cpf,s1)
cpf, v2 = getvalue(cpf,s2)
print(f'cpf {cpf}')
print(f'{(float(v1)+float(v2)):.2f}')