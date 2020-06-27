N = int(input())
A = list(map(int, input().split()))

A = sorted(A)
A = A + [-1]

ans = 0
total = 0
for i in range(N):
    total += A[i]

    if total >= A[i+1]/2:
        ans += 1
    else:
        ans = 0

print(ans)