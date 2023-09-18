l = int(input())
c = int(input())

cor = c%2

if l%2==0:
   cor = abs(1-cor)
print(cor)