from math import ceil

N, T = map(int, input().split())
A = list(map(int, input().split()))

time = sum(A)
print(ceil(time / T))