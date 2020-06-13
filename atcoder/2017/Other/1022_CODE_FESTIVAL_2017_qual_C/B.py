N = int(input())
A = list(map(int, input().split()))

ans = 3**N
cnt = 1
for i in range(N):
    if A[i]%2==0:
        cnt *= 2

print(ans-cnt)