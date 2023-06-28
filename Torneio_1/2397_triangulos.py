from math import acos, pi

A, B, C = input().split()
A, B, C = int(A), int(B), int(C)

if (A + B) <= C or (A + C) <= B or (B + C) <= A:
    print("n")
else:
    angA = acos((B ** 2 + C ** 2 - A ** 2) / (2 * B * C))
    angB = acos((A ** 2 + C ** 2 - B ** 2) / (2 * A * C))
    angC = acos((A ** 2 + B ** 2 - C ** 2) / (2 * A * B))

    if (angA == (pi / 2)) or (angB == (pi / 2)) or (angC == (pi / 2)):
        print("r")
    elif (angA > (pi / 2)) or (angB > (pi / 2)) or (angC > (pi / 2)):
        print("o")
    else:
        print("a")
