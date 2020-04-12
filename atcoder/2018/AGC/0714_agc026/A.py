N = int(input())
A = list(map(int, input().split()))
A += [100000]

cnt = 0
for i in range(N-1):
    if A[i+1] == A[i]:
        A[i+1] = 100000
        cnt += 1

print(cnt)