N = int(input())
a = list(map(int, input().split()))

from fractions import gcd

def lcm(m, n):
    return (m * n) // gcd(m, n)

def lcm_list(a):
    x = a[0]
    for i in range(1, len(a)):
        x = (x * a[i]) // gcd(x, a[i])
    return x

f = lcm_list(a)-1
ans = 0

for i in a:
    ans += f%i

print(ans)