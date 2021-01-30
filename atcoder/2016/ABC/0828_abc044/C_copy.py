N, A = map(int, input().split())
x = [i - A for i in list(map(int, input().split()))]

dp = [[0] * 5001 for _ in range(N)]
dp[0][2500] += 1
dp[0][x[0] + 2500] += 1
for i in range(1, N):
    for j in range(5000, -1, -1):
        dp[i][j] = dp[i - 1][j]
        if 0 <= j - x[i] <= 5000:
            dp[i][j] += dp[i - 1][j - x[i]]

print(dp[-1][2500] - 1)

print(dp[-1])