N = list(input())
N = [int(i) for i in N]

from itertools import product

ans = 0
for v in product([0, 1], repeat=len(N)):
    cnt = sum([N[i] for i in range(len(N)) if v[i]])
    # print(v, ':', cnt)
    if cnt % 3 == 0:
        ans = max(ans, sum(v))

if ans:
    print(len(N) - ans)
else:
    print(-1)