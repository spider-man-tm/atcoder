from itertools import (
    accumulate,  # 累積和のイテレータ
    groupby,  # 値をkey,同じ値の集まりをgroup
    permutations,  # 順列
    combinations,  # 組み合わせ
    product,  # 重複あり順列（直積）
)

n = int(input())
Sm, Sa, Sr, Sc, Sh = set(), set(), set(), set(), set()
for _ in range(n):
    s = input()
    if s[0]=='M':
        Sm.add(s)
    elif s[0]=='A':
        Sa.add(s)
    elif s[0]=='R':
        Sr.add(s)
    elif s[0]=='C':
        Sc.add(s)
    elif s[0]=='H':
        Sh.add(s)

ans = 0
S = [len(Sm), len(Sa), len(Sr), len(Sc), len(Sh)]

for v1, v2, v3 in combinations(S, 3):
    ans += v1*v2*v3

print(ans)