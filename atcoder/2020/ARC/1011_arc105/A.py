from itertools import product


cook = list(map(int, input().split()))

for v in product([0, 1], repeat=4):
    eat = 0
    not_eat = 0
    for i, vv in enumerate(v):
        if not vv:
            not_eat += cook[i]
        else:
            eat += cook[i]

    if eat == not_eat:
        print('Yes')
        exit()

print('No')