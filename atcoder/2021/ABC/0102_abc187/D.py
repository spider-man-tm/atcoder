N = int(input())
cnt = [[] for _ in range(N)]

aoki = 0
for i in range(N):
    a, b = map(int, input().split())
    cnt[i] = [a + b, -a, (a + b)-(-a)]
    aoki += a

cnt = sorted(cnt, key=lambda x: x[0], reverse=True)
cnt = sorted(cnt, key=lambda x: x[2], reverse=True)

taka = 0
for i in range(N):
    taka += cnt[i][0]
    aoki += cnt[i][1]
    if taka > aoki:
        print(i + 1)
        exit()
