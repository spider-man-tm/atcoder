n = int(input())
h = list(map(int, input().split()))
_list = [0] * 100
ans = 0

for i in range(n):
    _list[h[i]-1] += 1
    if sum(_list[h[i]:]) == 0:
        ans += 1

print(ans)