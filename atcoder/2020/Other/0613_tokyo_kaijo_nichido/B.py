A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())

diff = abs(A-B)

if (V-W)*T >= diff:
    print('YES')
else:
    print('NO')