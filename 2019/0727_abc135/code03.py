n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans, kurikosi = 0, 0
for i in range(n+1):
    if i != n:
        ans += min(a[i], kurikosi+b[i])
        if a[i]<=kurikosi:
            kurikosi = b[i]
        elif kurikosi < a[i] <= kurikosi+b[i]:
            kurikosi = kurikosi+b[i] - a[i]
        else:
            kurikosi = 0
    else:
        ans += min(kurikosi, a[i])

print(ans)