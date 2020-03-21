txa, tya, txb, tyb, T, V = map(int, input().split())
dist = T*V

n = int(input())
ans = False

for _ in range(n):
    x, y = map(int, input().split())
    d1 = (x-txa)**2 + (y-tya)**2
    d2 = (txb-x)**2 + (tyb-y)**2
    d = d1**(1/2) + d2**(1/2)
    if d <= dist:
        ans = True
        break

if ans:
    print('YES')
else:
    print('NO')