N, K, S = map(int, input().split())

if S != 10**9:
    ans = [S]*K + [S+1]*(N-K)
    print(*ans)
else:
    ans = [S]*K + [1]*(N-K)
    print(*ans)