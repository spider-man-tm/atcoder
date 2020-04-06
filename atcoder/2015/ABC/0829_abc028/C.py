import itertools

_list = list(map(int, input().split()))
ans = []

for v in itertools.combinations(_list, 3):
    ans.append(v[0]+v[1]+v[2])

ans = sorted(ans, reverse=True)
print(ans[2])