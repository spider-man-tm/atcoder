from itertools import (
    accumulate,  # 累積和のイテレータ
    groupby,  # 値をkey,同じ値の集まりをgroup
    permutations,  # 順列
    combinations,  # 組み合わせ
    product,  # 重複あり順列（直積, 深いネストにも使える）
    combinations_with_replacement,  # 重複あり組み合わせ
)

N = int(input())
L = list(map(int, input().split()))

def check(i, j, k):
    if i != j and j != k and k != i:
        maxi = max(i, j, k)
        total = i + j + k
        return maxi < total - maxi
    else:
        return 0


cnt = 0
for i, j, k in combinations(L, 3):
    cnt += check(i, j, k)

print(cnt)