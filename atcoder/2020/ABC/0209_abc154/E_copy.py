N = input()
K = int(input())
keta = len(N)

#[桁数][0以外の数字を使った回数-1][0:N以下が確定していない 1:N以下が確定している]
dp = [[[0]*2 for _ in range(K)] for _ in range(keta)]
dp[0][0][0] = 1
dp[0][0][1] = int(N[0]) - 1

for l in range(1, keta):
    for k in range(K):
        # 0追加
        if int(N[l]) == 0:
            dp[l][k][0] += dp[l-1][k][0]
        else:
            dp[l][k][1] += dp[l-1][k][0]
        dp[l][k][1] += dp[l-1][k][1]

        # 0以外追加
        if k > 0:
            if int(N[l]) > 0:
                dp[l][k][0] += dp[l-1][k-1][0]
                dp[l][k][1] += dp[l-1][k-1][0] * (int(N[l]) - 1)
            dp[l][k][1] += dp[l-1][k-1][1] * 9

    # その桁から始まる数
    dp[l][0][1] += 9

print(sum(dp[keta - 1][K - 1]))
