N = int(input())
A, B = [], []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

cnt = 0
for i in range(1, N+1):
    i *= -1
    a, b = A[i], B[i]
    a += cnt
    mod = a%b
    if mod != 0:
        cnt += b-mod
        
print(cnt)