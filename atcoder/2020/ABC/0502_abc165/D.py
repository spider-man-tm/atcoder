from math import ceil, floor

A, B, N = map(int, input().split())

if N>=B-1:
    x = B-1
    ans = floor((A*x)/B) - A*floor(x/B)
else:
    x = N
    ans = floor((A*x)/B) - A*floor(x/B)

print(ans)