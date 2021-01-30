N, M = map(int, input().split())
A = list(map(int, input().split()))
path = sorted([tuple(map(int, input().split())) for _ in range(M)])
dp = ['not'] * N
ans = -float('inf')

print('path:', path)

for x, y in path:
    x -= 1
    y -= 1
    tmp = A[x]
    
    if dp[x] != 'not':
        tmp = min(dp[x], tmp)

    if dp[y] != 'not':
        dp[y] = min(dp[y], tmp)
    else:
        dp[y] = tmp

    ans = max(ans, A[y] - tmp)

    print('x:', x, ' y:', y, ' tmp;', tmp, ' dp:', dp, '  ans:', ans)

print(ans)
