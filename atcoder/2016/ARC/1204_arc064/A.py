N, x = map(int, input().split())
A = list(map(int, input().split()))
A = [0] + A
total = sum(A)

for i in range(1, N+1):
    if A[i-1] + A[i] > x:
        tmp = (A[i-1]+A[i]) - x
        A[i] -= tmp
        
print(total - sum(A))