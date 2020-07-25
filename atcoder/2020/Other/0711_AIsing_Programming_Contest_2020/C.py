from itertools import (
    accumulate,  # 累積和のイテレータ
    groupby,  # 値をkey,同じ値の集まりをgroup
    permutations,  # 順列
    combinations,  # 組み合わせ
    product,  # 重複あり順列（直積, 深いネストにも使える）
    combinations_with_replacement,  # 重複あり組み合わせ
)

N = int(input())

ans = [0] * (10**5)

for i, j, k in product(list(range(1, 101)), repeat=3):
    tmp = i**2 + j**2 + k**2 + i*j + j*k + k*i
    ans[tmp] += 1

for i in range(1, N+1):
    print(ans[i])
