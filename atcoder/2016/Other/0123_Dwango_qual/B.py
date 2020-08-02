N = int(input())
K = list(map(int, input().split()))

ans = [[float('inf')] for _ in range(N)]

for i in range(N-1):
    ans[i].append(K[i])
    ans[i+1].append(K[i])

ans2 = []
for i in range(N):
    tmp = ans[i]
    ans2.append(min(tmp))

print(*ans2)