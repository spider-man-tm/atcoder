import numpy as np

N, M, X = map(int, input().split())
book = [list(map(int, input().split())) for _ in range(N)]

ans = 10**9

for i in range(1<<N):
    cost = 0
    tisiki = np.array([0]*M)
    cond = [0]*N
    for j in range(N):
        if 1&(i>>j):  # 右シフトして論理積（bit全探索）
            cond[j] = 1
    
    for k in range(N):
        if cond[k]==1:
            b = book[k]
            cost += b[0]
            tisiki += np.array(b[1:])
    
    if np.all(tisiki>=X):
        ans = min(ans, cost)

if ans < 10**9:
    print(ans)
else:
    print(-1)