N, C, K = map(int, input().split())
T = sorted([int(input()) for _ in range(N)])

cnt = 1
time = 0
capa = 1
pre = T[0]

for i in range(1, N):
    capa += 1
    time += T[i]-pre
    if capa>C or time>K:  # 次のバスを用意
        cnt += 1
        time = 0
        capa = 1

    pre = T[i]

print(cnt)