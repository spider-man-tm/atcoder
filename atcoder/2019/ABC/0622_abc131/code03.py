a, b, c, d = map(int, input().split())

def lcm(m, n):
    from fractions import gcd
    return (m * n) // gcd(m, n)

cd = lcm(c, d)

b_c = b//c
b_d = b//d
b_cd = b//cd
bb = b - (b_c + b_d - b_cd)

a_c = (a-1)//c
a_d = (a-1)//d
a_cd = (a-1)//cd
aa = (a-1) - (a_c + a_d - a_cd)

print(bb-aa)