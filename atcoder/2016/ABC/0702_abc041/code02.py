a, b, c = map(int, input().split())
mod = 10**9+7

a %= mod
b %= mod
c %= mod

ans = (a*b)%mod
ans = ans*c%mod
print(ans)