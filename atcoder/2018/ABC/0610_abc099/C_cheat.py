N = int(input())
dp = [0] * 100001


def func(dp, i, n):
    if i - n < 0:
        return float('inf')
    else:
        return dp[i-n] + 1

for i in range(1, 100001):
    t0 = dp[i-1] + 1
    t1 = func(dp, i, 6**1)
    t2 = func(dp, i, 6**2)
    t3 = func(dp, i, 6**3)
    t4 = func(dp, i, 6**4)
    t5 = func(dp, i, 6**5)
    t6 = func(dp, i, 6**6)
    t7 = func(dp, i, 9**1)
    t8 = func(dp, i, 9**2)
    t9 = func(dp, i, 9**3)
    t10 = func(dp, i, 9**4)
    t11 = func(dp, i, 9**5)
    dp[i] = min(t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11)

print(dp[N])