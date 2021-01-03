N = int(input())
edge = []
g = [list() for i in range(N)]
for i in range(N - 1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    edge.append((A, B))
    g[A].append(B)
    g[B].append(A)

'''
  0
  |
  1
 / \
2   3
    |
    4
'''
# print('edge: ', edge)
# edge:  [(0, 1), (1, 2), (1, 3), (3, 4)]
# print('g: ', g)
# g:  [[1], [0, 2, 3], [1], [1, 4], [3]]

depth = [-1] * N
depth[0] = 0
q = [0]
while q:
    at = q.pop()
    for i in g[at]:
        if depth[i] == -1:
            depth[i] = depth[at] + 1
            q.append(i)

# print('depth: ', depth)
# depth:  [0, 1, 2, 2, 3]

s = [0] * N
Q = int(input())
for i in range(Q):
    T, E, X = map(int, input().split())
    A, B = edge[E - 1]
    if depth[A] > depth[B]:
        # A,Bを入れ替え(Aの方が根に近い)
        A, B = B, A
        # 1,2を入れ替え
        T ^= 3
    if T == 1:
        s[0] += X
        s[B] -= X
    else:
        s[B] += X

# print('s: ', s)
# s:  [11, 99, 1000, 0, -10]
'''
  11
  |
  99
 /  \
1000 0
     |
    -10
'''

# いもす法的に累計和を取っていく
q = [0]
while q:
    at = q.pop()
    for i in g[at]:
        if depth[at] < depth[i]:
            s[i] += s[at]
            q.append(i)

# print('s: ', s)
# s:  [11, 110, 1110, 110, 100]

for i in s:
    print(i)
