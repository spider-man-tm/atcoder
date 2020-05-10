from itertools import combinations_with_replacement

N, M, Q = map(int, input().split())
q = []
for _ in range(Q):
    q.append(list(map(int, input().split())))

ans = 0
for v in combinations_with_replacement(range(1, M+1), N):
    score = 0
    for i in range(Q):
        joken = q[i]
        if v[joken[1]-1] - v[joken[0]-1] == joken[2]:
            score += joken[3]
    ans = max(ans, score)
    #print(v, ': ', score)

print(ans)