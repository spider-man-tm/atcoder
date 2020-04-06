n, T = map(int, input().split())
t = list(map(int, input().split()))

ans = 0
tmp = 0
for i in range(n):
    start, end = t[i], t[i]+T
    if start<tmp:
        ans += end-tmp
    else:
        ans += end-start
    tmp = end

print(ans)