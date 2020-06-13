H, W, _ = map(int, input().split())
L = [list(str(input())) for _ in range(H)]
ans = [[] * W for _ in range(H)]

k = 1  # イチゴの数
cnt = 1  # イチゴがない行の現在累積数

for h in range(H):
    if '#' not in L[h]:
        cnt += 1
    else:
        pre = -1
        for w in range(W):
            if L[h][w] == '#':
                for i in range(cnt):
                    ans[h-i].extend([k] * (w - pre))
                k += 1
                pre = w

        for i in range(cnt):
            ans[h-i].extend([k-1] * (W - 1 - pre))
        cnt = 1

cnt = 0
i = 1
while True:
    if '#' not in L[-i]:
        cnt += 1
        i += 1
    else:
        break
for i in range(cnt):
    ans[-cnt+i] = ans[-cnt-1]
for row in ans:
    print(*row)
