from statistics import median

N = int(input())
A, B = [], []

for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

mid_a = int(median(A))
mid_b = int(median(B))
ans = 0
for i in range(N):
    a, b = A[i], B[i]
    d1 = abs(a-mid_a)
    d2 = abs(b-a)
    d3 = abs(mid_b-b)
    ans += (d1+d2+d3)

print(ans)