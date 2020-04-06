N, K = map(int, input().split())
A = [int(input()) for _ in range(N)] + [0]
cnt, ans = 1, 0

for i in range(N):
    if A[i+1] > A[i]:
        cnt += 1
    else:
        if cnt >= K:
            ans += cnt-K+1
        cnt = 1

print(ans)