from math import gcd

N = int(input())

for _ in range(N):
    A, B = map(int, input().split())
    print(gcd(A, B))