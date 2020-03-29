from itertools import combinations

n = int(input())
d = list(map(int, input().split()))

total = 0
for a, b in combinations(d, 2):
    total += a*b

print(total)