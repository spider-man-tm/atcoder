N, x = map(int, input().split())
A = sorted(list(map(int, input().split())))

if x>sum(A):
    print(N-1)
    exit()

if x==sum(A):
    print(N)
    exit()

ans = 0
for i in range(N):
    if sum(A[:i]) <= x:
        ans = i
print(ans)