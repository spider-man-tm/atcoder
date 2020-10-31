from itertools import product

N = int(input())

for a, b in product(range(1, 38), range(1, 26)):
    if 3**a + 5**b == N:
        print(a, b)
        exit()

print(-1)
