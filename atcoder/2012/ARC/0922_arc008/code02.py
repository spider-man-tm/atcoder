from collections import Counter
from math import ceil, floor

N, M = map(int, input().split())
name = input()
kit = input()

name = [c for c in name]
kit = [c for c in kit]
name_c = Counter(name)
kit_c = Counter(kit)

ans = 0
for k, v in name_c.items():
    if k not in kit_c:
        print(-1)
        exit()
    else:
        tmp = ceil(v/kit_c[k])
        ans = max(ans, tmp)

print(ans)