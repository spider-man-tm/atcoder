N = int(input())
A = list(map(int, input().split()))
A = A + [-1]

def sum_return(n):
    return n*(n+1)//2

cnt = 0
ans = 0
pre = -1

for i in range(N+1):
    if A[i] > pre:
        cnt += 1
    else:
        ans += sum_return(cnt)
        cnt = 1
    pre = A[i]

print(ans)