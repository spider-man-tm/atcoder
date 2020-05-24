from collections import deque

def bfs_tree(graph, v=1):
    """
    graph: グラフ
    v: スタート
    """
    # 矢印がどこを向いているか
    # -1だと未探索
    arrow = [-1]*len(graph) 
    q = deque()
    q.append(v)
    arrow[v] = 0
    while q:
        now = q.popleft()
        for next_v in graph[now]:
            if arrow[next_v] != -1:
                continue
            else:
                q.append(next_v)
                arrow[next_v] = now
    return arrow

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
pre = []

for _ in range(M):
    A, B = map(int, input().split())
    graph[A-1].append(B-1)
    graph[B-1].append(A-1)

arrow = bfs_tree(graph, 0)

print('Yes')
for i in range(1, N):
    print(arrow[i]+1)