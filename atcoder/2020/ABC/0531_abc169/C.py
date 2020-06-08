from math import floor

A, B = input().split()
A = int(A)

B1 = int(B[:-3])
B2 = int(str(B)[-2:])

ans1 = A * B1
ans2 = A * B2 // 100

ans = ans1 + ans2
print(floor(ans))