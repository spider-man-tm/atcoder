N, Q = map(int, input().split())

grid = [[False]*N for _ in range(N)]

def print_grid(grid):
    for i in range(N):
        for j in range(N):
            if grid[i][j]:
                grid[i][j] = 'Y'
            else:
                grid[i][j] = 'N'
    for v in grid:
        print(*v, sep='')

for _ in range(Q):
    S = list(input().split())
    if S[0] == '1':
        a = int(S[1]) - 1
        b = int(S[2]) - 1
        grid[a][b] = True
    elif S[0] == '2':
        a = int(S[1]) - 1
        for i in range(N):
            if grid[i][a]:
                grid[a][i] = True
    else:
        a = int(S[1]) - 1
        tmp = []
        for i in range(N):
            if grid[a][i]:
                for j in range(N):
                    if grid[i][j] and j != a:
                        tmp.append([a, j])
        for a, j in tmp:
            grid[a][j] = True

print_grid(grid)