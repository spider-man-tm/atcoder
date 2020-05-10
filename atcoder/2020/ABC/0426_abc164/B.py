from math import ceil, floor

A, B, C, D = map(int, input().split())

takahashi = ceil(A/D)
aoki = ceil(C/B)

if takahashi>=aoki:
    print('Yes')
else:
    print('No')