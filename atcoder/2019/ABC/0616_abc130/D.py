N, K = map(int, input().split())
A = list(map(int, input().split()))

l, r = 0, 1
cnt = A[0]
ans = 0

while True:

    if l == r:
        r += 1
        cnt += A[r-1]

    else:
        if cnt >= K:
            ans += (N - r + 1)
            cnt -= A[l]
            l += 1
        else:
            if r < N:
                r += 1
                cnt += A[r-1]
            else:
                break

    if l == N:
        break

print(ans)