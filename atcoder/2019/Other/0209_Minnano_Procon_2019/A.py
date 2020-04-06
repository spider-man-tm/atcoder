N, K = map(int, input().split())
if N%2==0:
    n = N//2
else:
    n = N//2+1

if n>=K:
    print('YES')
else:
    print('NO')