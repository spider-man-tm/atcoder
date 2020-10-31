N = int(input())

ans = [5**i for i in range(1, 21)]

cnt = 1

for i in range(N):
    cnt += ans[i]

print(cnt)