N, M = map(int, input().split())
A = list(map(int, input().split()))

import itertools

ans = []

for i, _ in enumerate(A, 1):     
    for j in itertools.permutations(A, r=i):
        if len(j)>2:
            break
        elif len(j)==1:
            an = int(j[0]*2)
            ans.append(an)
        elif len(j)==2:
            an = int(j[0]+j[1])
            ans.append(an)

ans = sorted(ans, reverse=True)
ans = ans[:M]
ans = sum(ans)
print(ans)