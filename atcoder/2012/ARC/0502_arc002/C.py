from itertools import combinations, product

N = int(input())
c = input()
B = ['A', 'B', 'X', 'Y']
comb = []

for b1, b2 in product(B, B):
    comb.append(b1+b2)

ans = float('inf')
for c1, c2 in combinations(comb, 2):
    cc = c.replace(c1, 'L').replace(c2, 'R')
    ans = min(ans, len(cc))

print(ans)