n, k = map(int, input().split())
r = list(map(int, input().split()))

r = sorted(r, reverse=True)
r = sorted(r[:k])
ans = 0

for rate in r:
    ans = max(ans, (ans+rate)/2)

print(ans)