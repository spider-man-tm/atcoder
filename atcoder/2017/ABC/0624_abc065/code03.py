from math import factorial    #階乗計算
#print(math.factorial(5))   ->   120

N, M = map(int, input().split())
mod = 10**9+7

if abs(N-M)>=2:
    print(0)
    exit()

n = factorial(N)%mod
m = factorial(M)%mod
ans = n*m%mod

if N==M:
    print(ans*2%mod)
else:
    print(ans)