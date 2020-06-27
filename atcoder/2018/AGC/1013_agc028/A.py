from math import gcd

N, M = map(int, input().split())
S = input()
T = input()

def lcm(m, n):
    return (m * n) // gcd(m, n)

lc = lcm(N, M)

ss = lc//N
tt = lc//M

for i in range(1, lc+1, ss*tt):
    s_tmp = (i - 1) // ss
    t_tmp = (i - 1) // tt

    if S[s_tmp] != T[t_tmp]:
        print(-1)
        exit()

print(lc)