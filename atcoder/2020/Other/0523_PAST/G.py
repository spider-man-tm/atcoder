from collections import deque

N, X, Y = map(int, input().split())
visited = [[-1]*500 for _ in range(500)]
X += 250
Y += 250


for _ in range(N):
    x, y = map(int, input().split())
    visited[x+250][y+250] = '#'

def bfs(gy,gx,visited):
    visited[250][250] = 0
    Q = deque([])
    Q.append([250, 250])
    while Q:
        y,x = Q.popleft()
        if [y, x] == [gy, gx]:
            return visited[y][x]
 
        for i,j in [(-1,0),(0,1),(1,1),(1,0),(-1,1),(0,-1)]:
            try:
                if visited[y+i][x+j] != '#' and visited[y+i][x+j] == -1:
                    # 探索可能かつ未探索の場合
                    visited[y+i][x+j] = visited[y][x]+1
                    Q.append([y+i,x+j])
            except:
                pass

ans = bfs(X, Y, visited)
if ans:
    print(ans)
else:
    print(-1)