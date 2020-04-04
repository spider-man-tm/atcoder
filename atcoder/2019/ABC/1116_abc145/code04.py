x, y = map(int, input().split())

if (x+y)%3 != 0:
    print(0)
    exit()

m = (2*x - y)//3
n = (2*y - x)//3

if m<0 or n<0:
    print(0)
    exit()

"""Combination(mod付き)の高速計算"""
def extgcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extgcd(b, a % b)
        x -= (a // b) * y
        return d, y, x
    
def modinv(a, mod): 
    return extgcd(a, mod)[1] % mod

def modcomb(n, k, mod):
    q, a = 1, 1
    for i in range(n-k+1, n+1):
        q = (q * i) % mod
    for i in range(2, k+1):
        a = (a * i) % mod
    return int(q * modinv(a, mod) % mod)

ans = modcomb(n+m, m, 10**9+7)
print(ans)