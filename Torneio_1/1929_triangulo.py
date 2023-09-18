a, b, c, d = input().split()
a, b, c, d = int(a), int(b), int(c), int(d)

if (a + b) > c and (a + c) > b and (b + c) > a:
    print("S")
elif (a + b) > d and (a + d) > b and (b + d) > a:
    print("S")
elif (a + c) > d and (a + d) > c and (c + d) > a:
    print("S")
elif (b + c) > d and (b + d) > c and (c + d) > b:
    print("S")
else:
    print("N")
