from collections import Counter

N, K = map(int, input().split())
A = list(map(int, input().split()))
C = Counter(A)

ball = []
for k, v in C.items():
    ball.append([v, k])
ball.sort(key=lambda x: -x[0])

ans = 0
for i in range(len(ball)):
    if i>=K:
        ans += ball[i][0]

print(ans)