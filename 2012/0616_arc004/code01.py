N = int(input())
p = [list(map(int, input().split())) for _ in range(N)]

def dist(i, j):
    return (p[i][0] - p[j][0])**2 + (p[i][1] - p[j][1])**2

ans = 0
for i in range(N):
    for j in range(N):
        ans = max(ans, dist(i, j))

print(ans**(1/2))