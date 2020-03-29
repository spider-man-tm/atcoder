n = int(input())
a = []

for _ in range(n):
    a.append(int(input()))

b = sorted(a, reverse=True)

for i in range(n):
    if a[i] == b[0]:
        print(b[1])
    else:
        print(b[0])