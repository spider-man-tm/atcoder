from collections import Counter

N = int(input())
T = sorted([int(input()) for _ in range(N)])

mod = 10**9 + 7
def f(n):
  ret = 1
  for i in range(1, n+1):
    ret = ret * i % mod
  return ret

S = [0]*(N+1)
pena = 0
for i in range(1, N+1):
  S[i] = S[i-1] + T[i-1]
pena = sum(S)

c = Counter(T)
sol = 1
for val in c.values():
  sol = f(val) * sol % mod

print(pena)
print(sol)