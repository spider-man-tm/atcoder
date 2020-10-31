N = int(input())

ans = 0

for _ in range(N):
    _list = map(int, input().split())
    if sum(_list) < 20:
        ans += 1

print(ans)