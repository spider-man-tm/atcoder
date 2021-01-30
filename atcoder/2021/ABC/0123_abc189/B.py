N, X = map(int, input().split())
X *= 100

cnt = 0
for i in range(N):
    V, P = map(int, input().split())
    cnt += V * P

    if cnt > X:
        print(i + 1)
        exit()

print(-1)