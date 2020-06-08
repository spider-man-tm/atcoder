N, L = map(int, input().split())
X = [False] * (L+10)
hard = list(map(int, input().split()))

for x in hard:
    X[x] = True

T1, T2, T3 = map(int, input().split())

dp = [float('inf')]*(L+10)
dp[0] = 0

for i in range(L+1):
    cost = T3 if X[i] else 0
    dp[i+1] = min(dp[i+1], dp[i] + T1 + cost)
    dp[i+2] = min(dp[i+2], dp[i] + T1 + T2 + cost)
    dp[i+4] = min(dp[i+4], dp[i] + T1 + T2*3 + cost)
    if i+1 == L:
        dp[i+1] = min(dp[i+1], dp[i] + T1//2 + T2//2 + cost)
    elif i+2 == L:
        dp[i+2] = min(dp[i+2], dp[i] + T1//2 + 3*T2//2 + cost)
    elif i+3 == L:
        dp[i+3] = min(dp[i+3], dp[i] + T1//2 + 5*T2//2 + cost)
 
print(dp[L])