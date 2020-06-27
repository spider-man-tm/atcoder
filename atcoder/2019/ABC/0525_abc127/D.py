N, M = map(int, input().split())
A = list(map(int, input().split()))

dic = {}
for i in range(N):
    tmp = A[i]
    if tmp in dic:
        dic[tmp] += 1
    else:
        dic[tmp] = 1

for _ in range(M):
    B, C = map(int, input().split())
    if C in dic:
        dic[C] += B
    else:
        dic[C] = B

dic = sorted(dic.items(), reverse=True)

ans, cnt = 0, 0
i = 0
while True:
    k, v = dic[i]
    cnt += v
    if cnt < N:
        ans += k*v
    elif cnt == N:
        ans += k*v
        break
    else:
        ans += k*(v - (cnt-N))
        break
    i += 1

print(ans)