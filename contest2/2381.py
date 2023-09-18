n = int(input())
for i in range(n):
    s = input().split()
    s = set(s)
    s = list(s)
    s = sorted(s)
    s = ' '.join(s)
    print(s)

