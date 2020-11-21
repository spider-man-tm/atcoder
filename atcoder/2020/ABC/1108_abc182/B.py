N = int(input())
A = list(map(int, input().split()))
ans = [0, 0]

for i in range(2, max(A)+1):
    cnt = 0
    for j in range(N):
        if A[j] % i == 0:
            cnt += 1

    if cnt >= ans[1]:
        ans = [i, cnt]

print(ans[0])