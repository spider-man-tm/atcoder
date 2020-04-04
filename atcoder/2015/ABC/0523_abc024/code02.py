n, t = map(int, input().split())
ans, end = 0, 0
for _ in range(n):
    a = int(input())
    if a>=end:
        ans += t
    else:
        ans += (a+t-end)
    end = a+t

print(ans)