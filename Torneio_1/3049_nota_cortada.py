b = int(input()) #comprimento base
t = int(input()) #comprimento da outra base

# area trapezio:
# (base menor + base maior)*altura/2
area_felix = ((b+t)*70)/2

meia_area = 70*160/2

if area_felix > meia_area:
    print(1) 
elif area_felix < meia_area:
    print(2)
else:
    print(0)
