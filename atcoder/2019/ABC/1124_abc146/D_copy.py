from collections import deque

N = int(input())
graph = [[] for _ in range(N)]

for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a-1].append([b-1, i])
    graph[b-1].append([a-1, i])

print('graph: ', graph)

ans = [0] * (N - 1)
Q = deque([[1, 0, -1]])

while Q:
    #print(Q)
    v, p_color, root = Q.popleft()
    #print('v: ', v)
    #print('p_color: ', p_color)
    #print('root', root)
    cnt = 1
    for node in graph[v]:
        #print('node', node)
        if node[0] == root:
            continue
        if cnt == p_color:
            cnt += 1
        ans[node[1]] = cnt
        Q.append([node[0], cnt, v])
        cnt += 1
    #print()


print(max(ans))
print(*ans, sep='\n')