n = int(input())
h = list(map(int, input().split()))

cnt = 0
before = 0

for i in range(n):
    if before < h[i]:
        cnt += h[i] - before
    before = h[i]
    # print('before: ', before)
    # print('cnt: ', cnt)

print(cnt)