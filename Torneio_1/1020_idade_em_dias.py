dias = int(input()) #registra numero de dias

# a quantidade de anos será a divisão inteira dos
# dias pelo numero de dias em um ano
anos = dias//365


# a quantidade de meses será o que sobrou dos dias depois dos anos
# que pode ser obtido pela operação resto, divido
# pela quantidade de dias em um mes
meses = (dias%365)//30

# a quantidade de dias será o que sobrou dos dias
# depois dos anos e dos meses
dias = (dias%365)%30

print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")
