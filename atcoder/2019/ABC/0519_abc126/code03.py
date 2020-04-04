n, k = map(int, input().split())
p = [0] * n

for i in range(1, n+1):
    score = i
    cnt = 0
    while score < k:
        score *= 2
        cnt += 1
    if cnt==0:
        proba = 1.0
    else:
        proba = (1/2)**cnt
    p[i-1] = proba

ans = 0
for pp in p:
    ans += (1/n)*pp

print(ans)