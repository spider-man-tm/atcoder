from itertools import (
    accumulate,  # 累積和のイテレータ
    groupby,  # 値をkey,同じ値の集まりをgroup
    permutations,  # 順列
    combinations,  # 組み合わせ
    product,  # 重複あり順列（直積, 深いネストにも使える）
)

N = int(input())
A = [list(map(int, input().split())) for _ in range(N-1)]
ans = -float('inf')

# 3**N組み合わせを列挙
for pattern in product([0, 1, 2], repeat=N):

    # pattern: 長さNのタプル
    g1, g2, g3 = [], [], []
    for idx, key in enumerate(pattern):
        if key==0:
            g1.append(idx)
        elif key==1:
            g2.append(idx)
        else:
            g3.append(idx)

    happy = 0
    for g in [g1, g2, g3]:
        for i, j in combinations(g, 2):
            happy += A[i][j-i-1]
    ans = max(ans, happy)

print(ans)