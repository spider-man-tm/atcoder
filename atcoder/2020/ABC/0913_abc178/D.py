S = int(input())
mod = 10**9 + 7

if S < 3:
    print(0)
else:
    dp = [0] * (S+1)
    dp[0] = 1
    dp[1] = 0
    dp[2] = 0
    for i in range(3, S+1):
        dp[i] = (dp[i-1] + dp[i-3]) % mod
    print(dp[-1])