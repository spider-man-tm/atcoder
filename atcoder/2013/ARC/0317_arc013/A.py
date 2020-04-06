from itertools import (
    accumulate,  # 累積和のイテレータ
    groupby,  # 値をkey,同じ値の集まりをgroup
    permutations,  # 順列
    combinations,  # 組み合わせ
    product,  # 重複あり順列（直積, 深いネストにも使える）
)

N, M, L = map(int, input().split())
P, Q, R = map(int, input().split())
ans = 0

for p, q, r in permutations([P, Q, R], 3):
    ans = max(ans, (N//p)*(M//q)*(L//r))

print(ans)