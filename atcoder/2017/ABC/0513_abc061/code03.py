N, K = map(int, input().split())
l = [0]*(10**5+1)

for _ in range(N):
    a, b = map(int, input().split())
    l[a] += b

total = 0
for i, n in enumerate(l):
    total += n
    if total>=K:
        print(i)
        break