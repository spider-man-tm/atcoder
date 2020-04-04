n, m = map(int, input().split())
shop = []
for _ in range(n):
    a, b = map(int, input().split())
    shop.append([a, b])

shop = sorted(shop)
ans, num = 0, 0
for i in range(n):
    a, b = shop[i]
    num += b
    ans += a*b
    if num>=m:
        ans -= (num-m)*a
        break

print(ans)