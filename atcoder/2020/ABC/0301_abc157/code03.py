N, M = map(int, input().split())
sc = [list(map(int, input().split())) for _ in range(M)]

for i in range(1000):
    flag = True
    i = str(i)
    if len(i) != N:
        continue

    for s, c in sc:
        if int(i[s-1]) != c:
            flag = False
            break
    if flag:
        print(int(i))
        exit()

print(-1)