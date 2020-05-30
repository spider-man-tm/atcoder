N, M, Q = map(int, input().split())

graph = [[] for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    u -= 1;  v -= 1
    graph[u].append(v)
    graph[v].append(u)

c = list(map(int, input().split()))

for _ in range(Q):
    query = list(map(int, input().split()))
    if len(query)==2:
        x = query[1]-1
        print(c[x])
        for node in graph[x]:
            c[node] = c[x]
    else:
        x = query[1]-1
        y = query[2]
        print(c[x])
        c[x] = y