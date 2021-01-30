N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

memo = [0] * N
memo[0] = a[0] * b[0]
a_max = a[0]
b_max = b[0]
best = a_max * b_max

for i in range(1, N):
    a_max = max(a_max, a[i])
    best = max(best, a_max * b[i])
    memo[i] = best

for m in memo:
    print(m)
