from itertools import (
    accumulate,  # 累積和のイテレータ
    groupby,  # 値をkey,同じ値の集まりをgroup
    permutations,  # 順列
    combinations,  # 組み合わせ
    product,  # 重複あり順列（直積）
)
A = list(map(int, input().split()))

ans = float('inf')
for a1, a2, a3 in permutations(A, 3):
    tmp = abs(a2-a1)+abs(a3-a2)
    ans = min(ans, tmp)

print(ans)