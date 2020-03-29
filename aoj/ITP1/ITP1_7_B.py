from itertools import (
    accumulate,  # 累積和のイテレータ
    groupby,  # 値をkey,同じ値の集まりをgroup
    permutations,  # 順列
    combinations,  # 組み合わせ
    product,  # 重複あり順列（直積, 深いネストにも使える）
)

while True:
    n, x = map(int, input().split())
    if n==0 and x==0:
        break
    ans = 0
    for a, b, c in combinations(list(range(1, n+1)), 3):
        if a+b+c==x:
            ans += 1
    print(ans)