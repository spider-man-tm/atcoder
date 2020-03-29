from fractions import gcd

def lcm(m, n):
    return (m * n) // gcd(m, n)

def lcm_list(a):
    x = a[0]
    for i in range(1, len(a)):
        x = (x * a[i]) // gcd(x, a[i])
    return x


N = int(input())
T = [int(input()) for _ in range(N)]
print(lcm_list(T))