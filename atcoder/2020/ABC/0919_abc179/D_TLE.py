import numpy as np

mod = 998244353

N, K = map(int, input().split())
LR = []
lmin = float('inf')

for _ in range(K):
    l, r = map(int, input().split())
    LR.append((l, r))
    lmin = min(lmin, l)

dp = np.array([0] * (N+1))
dp[1] += 1

for i in range(1, N-lmin+1):
    now = dp[i] % mod
    if now:
        for l, r in LR:
            if l <= N:
            # try:
                dp[i+l:min(N+1, i+r+1)] += now
            # except:
            else:
                break

print(dp[-1] % mod)
