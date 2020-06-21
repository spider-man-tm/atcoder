N = int(input())
A = list(map(int, input().split()))

A = sorted(A)
maxi = 10**6+1
dp = [0] * maxi

for i in range(N):
    tmp = A[i]
    if dp[tmp] != 0:
        dp[tmp] = 2
        continue
    else:
        for j in range(tmp, maxi, tmp):
            dp[j] += 1

ans = 0
for i in range(N):
    tmp = A[i]
    if dp[tmp] == 1:
        ans += 1

print(ans)