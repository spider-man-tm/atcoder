from itertools import combinations

N = int(input())
ans = 0
p = []

for _ in range(N):
    x, y = map(int, input().split())
    p.append([x, y])

for v in combinations(p, 2):
    difx = v[0][0] - v[1][0]
    dify = v[0][1] - v[1][1]

    if abs(dify) <= abs(difx):
        ans += 1

print(ans)