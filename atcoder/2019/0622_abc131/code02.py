n, l = map(int, input().split())
apple = [i for i in range(l, l+n)]
total = sum(apple)

ans = float('inf')
ans2 = 0
for i in range(n):
    tmp = total - apple[i]
    if ans > abs(total - tmp):
        ans = abs(total - tmp)
        ans2 = tmp

print(ans2)