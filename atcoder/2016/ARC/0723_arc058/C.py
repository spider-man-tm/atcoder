N, K = map(int, input().split())
D = list(input().split())

ans = N
for p in range(N, N+10**9):
    flag = True
    s = str(p)
    for c in s:
        if c in D:
            flag = False
            break

    if flag:
        break

print(s)