n, m = map(int, input().split())

for i in range(n):
    if i == 0:
        k = list(map(int, input().split()))[1:]
        k = set(k)

    else:
        tmp = list(map(int, input().split()))[1:]
        tmp = set(tmp)
        k = k & tmp

print(len(k))