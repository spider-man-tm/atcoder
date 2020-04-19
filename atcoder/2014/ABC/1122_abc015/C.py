from itertools import product

N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]

for v in product(range(K), repeat=N):
    for i, j in enumerate(v):
        if i == 0:
            ans = T[i][j]
        else:
            ans ^= T[i][j]

    if ans == 0:
        print('Found')
        exit()

print('Nothing')