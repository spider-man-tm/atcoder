N = int(input())
A = list(map(int, input().split()))

total = [0] * N
pre = 0
for i in range(N):
    total[i] = pre + A[i]
    pre = total[i]

start = [0] * N
pre = 0
for i in range(N-1):
    start[i+1] = start[i]+ total[i]

maxi = [0] * N
maxi[0] = total[0]
for i in range(1, N):
    maxi[i] = max(maxi[i-1], total[i])

ans = 0
for i in range(N):
    tmp = start[i]
    tmp = max(tmp, tmp+maxi[i])
    ans = max(ans, tmp)
    
print(ans)