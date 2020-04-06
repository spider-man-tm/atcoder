from collections import deque
#S = deque(['x', 'y'])
#print(S)   ->   deque(['x', 'y'])

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
sy, sx, gy, gx = sy-1, sx-1, gy-1, gx-1
c = [[c for c in input()] for _ in range(R)]
visited = [[-1]*C for _ in range(R)]


def bfs(sy, sx, gy, gx, c, visited):
    visited[sy][sx] = 0
    Q = deque([])
    Q.append([sx, sy])
    while Q:
        y,x = Q.popleft()

        if [y, x] == [gy, gx]:
            return visited[y][x]

        for i, j in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            if c[y+i][x+j] == '.' and visited[y+i][x+j] == -1:
                # 探索可能かつ未探索の場合
                visited[y+i][x+j] = visited[y][x]+1
                Q.append([y+i,x+j])


print(bfs(sy, sx, gy, gx, c, visited))