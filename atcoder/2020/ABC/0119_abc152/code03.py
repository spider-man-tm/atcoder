n = int(input())
p = list(map(int, input().split()))

ans = 0
min_n = 0
for i in range(len(p)):
    if i==0:
        ans += 1
        min_n = p[i]
    else:
        if p[i] <= min_n:
            ans += 1
            min_n = p[i]
        else:
            pass

print(ans)