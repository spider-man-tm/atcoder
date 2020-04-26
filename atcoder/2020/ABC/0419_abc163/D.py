N, K = map(int, input().split())
mod = 10**9+7

sum_left = list(range(N+1))
sum_right = list(range(N+1))[::-1]

for i in range(1, N+1):
    sum_left[i] += sum_left[i-1]

for i in range(1, N+1):
    sum_right[i] += sum_right[i-1]

ans = 0
for i in range(K-1, N+1):
    ans += sum_right[i] - sum_left[i] + 1
    ans %= mod

print(ans)