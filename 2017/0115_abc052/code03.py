n = int(input())
mod = 10**9+7
s = [0] * (n+1)

for i in range(2, n+1):
    p = 2
    while i>1:
        while i%p==0:
            i //= p
            s[p] += 1
        p += 1

ans = 1
for i in s:
    ans *= i+1
    ans %= mod

print(ans)