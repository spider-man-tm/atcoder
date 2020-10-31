A, B, C = map(int, input().split())

mod = 998244353

ans = int((1+C) * (C/2)) % mod
print(ans)
ans *= int((1+B) * (B/2))
ans %= mod
print(ans)
ans *= int((1+A) * (A/2))
ans %= mod
print(ans)