n = int(input())
ab = []
for _ in range(n):
    a, b = map(int, input().split())
    ab.append([b, a])

ab = sorted(ab)
total = 0

for i in range(n):
    b, a = ab[i]
    total += a
    if total>b:
        print('No')
        exit()

print('Yes')