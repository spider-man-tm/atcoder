from itertools import product

n, c = map(int, input().split())
a = [int(input()) for _ in range(n)]
eve = a[::2]
odd = a[1::2]

cnt = float('inf')
for c1, c2 in product(range(1, 11), repeat=2):
    if c1 != c2:
        cnt1 = len(eve) - eve.count(c1)
        cnt2 = len(odd) - odd.count(c2)
        cnt = min(cnt, cnt1+cnt2)

print(cnt*c)