N, A, B = map(int, input().split())
cnt = 0
for _ in range(N):
    t = int(input())
    if t < A:
        cnt += 1
    elif t >= B:
        cnt += 1

print(cnt)
