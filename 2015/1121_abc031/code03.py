n = int(input())
a = list(map(int, input().split()))

ans = {}
for i in range(n):
    aoki = -3000
    for j in range(n):
        if j==i:
            continue
        
        start = min(i, j)
        end = max(i, j)

        l1 = sum(a[start:end+1:2])
        l2 = sum(a[start+1:end+1:2])

        if l2 > aoki:
            aoki = l2
            ans[i] = l1

maxi = -3000
for k, v in ans.items():
    if v > maxi:
        maxi = v

print(maxi)