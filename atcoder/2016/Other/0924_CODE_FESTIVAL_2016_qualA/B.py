N = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(N):
    ai = a[i]-1
    if a[ai]==i+1:
        ans += 0.5

print(int(ans))