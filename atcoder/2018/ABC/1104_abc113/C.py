N, M = map(int, input().split())
P = [[] for _ in range(N+1)]
ite = []

for _ in range(M):
    p, y = map(int, input().split())
    P[p].append(y)
    ite.append([p, y])

dic = {}
for p in range(N+1):
    P[p] = sorted(P[p])
    for i, y in enumerate(P[p]):
        i += 1
        dic[y] = '{}{}'.format(str(p).zfill(6), str(i).zfill(6))

for i in range(M):
    p, y = ite[i]
    print(dic[y])