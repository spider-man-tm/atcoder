from math import floor

X, Y = map(int, input().split())

if not Y:
    print('ERROR')
else:
    ans = floor(X * 100 // Y) / 100
    print(f'{ans:.2f}')