h, n = map(int, input().split())
a = list(map(int, input().split()))

hi = sum(a)

if h>hi:
    print('No')
else:
    print('Yes')