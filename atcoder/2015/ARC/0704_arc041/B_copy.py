N, M = map(int, input().split())
B = [[int(c) for c in input()] for _ in range(N)]
ans = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if B[i][j] != 0:
            tmp = B[i][j]
            ans[i+1][j] += tmp
            B[i][j] -= tmp
            B[i+1][j-1] -= tmp
            B[i+1][j+1] -= tmp
            B[i+2][j] -= tmp
        
for a in ans:
    print(*a, sep='')