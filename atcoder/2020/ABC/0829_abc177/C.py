N = int(input())
A = sorted(list(map(int, input().split())))

ans = 0
MOD = 10**9+7
total = sum(A)

for i in range(N-1):
    tmp = A[i]
    total -= tmp
    ans += (tmp * total) % MOD
    ans %= MOD

print(ans)