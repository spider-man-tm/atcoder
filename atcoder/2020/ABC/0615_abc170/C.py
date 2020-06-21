X, N = map(int, input().split())

try:
    p = list(map(int, input().split()))
except EOFError:
    print(X)
    exit()

i = 0
while True:
    tmp1 = X - i
    tmp2 = X + i

    if tmp1 not in p:
        print(tmp1)
        exit()
    if tmp2 not in p:
        print(tmp2)
        exit()

    i += 1