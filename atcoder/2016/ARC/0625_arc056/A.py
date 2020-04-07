from math import ceil, floor

A, B, K, L = map(int, input().split())

p1 = A*K
p2 = ceil(K/L)*B

set_n = floor(K/L)
p3 = set_n*B + (K-set_n*L)*A

print(min(p1, p2, p3))