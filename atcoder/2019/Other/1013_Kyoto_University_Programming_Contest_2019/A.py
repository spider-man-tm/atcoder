N, X = map(int, input().split())
a = list(map(int, input().split()))

amax = max(a)
ans = 0
for i in range(N):
    if a[i] >= amax - X:
        ans += 1

print(ans)