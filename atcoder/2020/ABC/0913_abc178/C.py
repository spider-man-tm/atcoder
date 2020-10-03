N = int(input())
MOD = 10**9 + 7
a1, a2, a3 = 1, 1, 1

for _ in range(N):
    a1 *= 10
    a1 %= MOD

for _ in range(N):
    a2 *= 9
    a2 %= MOD
a2 *= 2
a2 %= MOD

for _ in range(N):
    a3 *= 8
    a3 %= MOD

ans = a1 - a2 + a3
ans %= MOD
print(ans)
