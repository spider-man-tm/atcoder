n = int(input())
a = list(map(int, input().split()))

if n%2==0:
    odd = list(range(1, n, 2))
    eve = list(reversed(list(range(2, n+1, 2))))
    ix = eve+odd
    for i in ix:
        print(a[i-1], end=' ')

else:
    odd = list(reversed(list(range(1, n+1, 2))))
    eve = list(range(2, n, 2))
    ix = odd+eve
    for i in ix:
        print(a[i-1], end=' ')

print()