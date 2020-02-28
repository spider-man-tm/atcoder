import math

n, a, b = map(int, input().split())


def cmb(n, r, mod):
    c=1
    for i in range(1, r+1):
        c = (c * (n-i+1) * pow(i, mod-2, mod)) % mod
    return c


mod = 10**9+7

ans = pow(2, n, mod)
ans -= 1
ans -= cmb(n, a, mod)
ans -= cmb(n, b, mod)

while ans<0:
    ans+=mod
    
print(ans)