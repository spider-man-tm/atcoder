from itertools import (
    accumulate,  # 累積和のイテレータ
    groupby,  # 値をkey,同じ値の集まりをgroup
    permutations,  # 順列
    combinations,  # 組み合わせ
    product,  # 重複あり順列（直積, 深いネストにも使える）
)

N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for p1, p2, p3 in combinations(P, 3):
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    x3, y3 = p3[0], p3[1]
    x2, y2 = x2-x1, y2-y1
    x3, y3 = x3-x1, y3-y1
    s = abs(x2*y3 - x3*y2)
    if s%2==0 and s!=0:
        ans += 1

print(ans)