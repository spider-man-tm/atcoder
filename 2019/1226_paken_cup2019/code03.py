n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

from itertools import (
    accumulate,  # 累積和のイテレータ
    groupby,  # 値をkey,同じ値の集まりをgroup
    permutations,  # 順列
    combinations,  # 組み合わせ
    product,  # 重複あり順列（直積）
)

ans = 0
for j1, j2 in combinations(list(range(m)), 2):
    total_socre = 0
    for i in range(n):
        score = max(A[i][j1], A[i][j2])
        total_socre += score
    ans = max(total_socre, ans)

print(ans)