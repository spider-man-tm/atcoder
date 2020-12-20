N = int(input())
A, B, C = input(), input(), input()

ans = 0
for i in range(N):
    a, b, c = A[i], B[i], C[i]
    if len(set([a, b, c])) == 2:
        ans += 1
    elif len(set([a, b, c])) == 3:
        ans += 2

print(ans)