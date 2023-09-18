p, n = input().split()
canos = input().split()
canos = [canos[0]] + canos
p = int(p)
n = int(n)
consegue = True
for i in range(1, n+1):
    if abs(int(canos[i])-int(canos[i-1]))>p:
        consegue=False
        break
if consegue:
    print("YOU WIN")
else:
    print("GAME OVER")
    