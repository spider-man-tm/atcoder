from itertools import combinations

N, X, Y = map(int, input().split())
S = [list(reversed(list(range(1, i+1)))) + list(range(N-i)) for i in range(N)]

S[X-1][Y-1] = 1
S[Y-1][X-1] = 1

for i in range(N):
    for j in range(N):
        x, y = X-1, Y-1
        S[i][j] = min(S[i][j], S[i][x]+1+S[y][j])

dist = [0]*N
for i, j in combinations(list(range(N)), 2):
    d = S[i][j]
    dist[d] += 1

for i in range(1, len(dist)):
    print(dist[i])