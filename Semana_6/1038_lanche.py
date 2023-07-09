valores = [4.0, 4.5, 5.0, 2.0, 1.5]
cod, quant = input().split()
cod, quant = int(cod), int(quant)

print(f"Total: R$ {valores[cod - 1] * quant:.2f}")
