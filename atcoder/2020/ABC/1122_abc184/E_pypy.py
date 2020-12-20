from collections import deque

H, W = map(int, input().split())
maze = ['#'+input()+'#' for _ in range(H)]
maze = ['#'*(W+2)] + maze + ['#'*(W+2)]

visited = [[-1]*(W+2) for _ in range(H+2)]

sx, sy, gy, gx = 0, 0, 0, 0
warp = {}
done_warp = set()

def helper(v):
    for i in range(len(v)):
        print(*v[i])

for i in range(1, H+2):
    for j in range(1, W+2):
        if maze[i][j] == 'S':
            sy, sx = i, j
        elif maze[i][j] == 'G':
            gy, gx = i, j
        elif maze[i][j] != '.' and maze[i][j] != '#':
            if maze[i][j] in warp:
                warp[maze[i][j]].append([i, j])
            else:
                warp[maze[i][j]] = []
                warp[maze[i][j]].append([i, j])


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

        # ワープマス
        if c[y][x] != '.' and c[y][x] != 'S':
            tmp = c[y][x]
            if tmp not in done_warp:
                for i, j in warp[tmp]:
                    if i != y or j != x:
                        if visited[i][j] == -1:
                            visited[i][j] = visited[y][x]+1
                            Q.append([i, j])
                done_warp.add(tmp)

ans = bfs(sy, sx, gy, gx, maze, visited)

if ans:
    print(ans)
else:
    print(-1)
