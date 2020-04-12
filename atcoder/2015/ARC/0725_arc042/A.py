N, M = map(int, input().split())
A = [int(input()) for _ in range(M)][::-1]
l = [0]*(N+1)
ans = []
for i in range(M):
    tmp = A[i]
    if l[tmp]==0:
        ans.append(tmp)
        l[tmp] = 1

dif = {i for i in range(1, N+1)} - set(ans)
ans += sorted(list(dif))

for i in ans:
    print(i)