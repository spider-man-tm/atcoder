from itertools import product

N, M = map(int, input().split())
joken = [list(map(int, input().split())) for _ in range(M)]
K = int(input())
man = [list(map(int, input().split())) for _ in range(K)]


def return_dish(v, man, n):
    dish = [0] * n
    for i in range(len(v)):
        dish[man[i][v[i]]-1] += 1

    return dish

def check_count(dish, joken):
    cnt = 0
    for v in joken:
        if dish[v[0]-1] and dish[v[1]-1]:
            cnt += 1

    return cnt


ans = 0
for v in product([0, 1], repeat=K):
    dish = return_dish(v, man, N)
    ans = max(ans, check_count(dish, joken))

print(ans)
