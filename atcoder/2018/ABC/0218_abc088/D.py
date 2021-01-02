from collections import deque

H, W = map(int, input().split())
maze = ['#'+input()+'#' for _ in range(H)]
maze = ['#'*(W+2)] + maze + ['#'*(W+2)]

visited = [[-1]*(W+2) for _ in range(H+2)]

sx, sy, gy, gx = 1, 1, H, W

def helper(v):
    for i in range(len(v)):
        print(*v[i])


def bfs(sy, sx, gy, gx, c, visited):
    visited[sy][sx] = 0
    Q = deque([])
    Q.append([sy, sx])
    while Q:
        y, x = Q.popleft()
 
        if [y, x] == [gy, gx]:
            return visited[y][x]

        for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if c[y+i][x+j] != '#' and visited[y+i][x+j] == -1:
                # 探索可能かつ未探索の場合
                visited[y+i][x+j] = visited[y][x]+1
                Q.append([y+i, x+j])


n_step = bfs(sy, sx, gy, gx, maze, visited)

if n_step:
    cnt = 0
    for i in range(1, H+1):
        line = maze[i]
        line = line[1:-1]
        cnt += line.count('#')

    print(H*W - (n_step+1) - cnt)
else:
    print(-1)