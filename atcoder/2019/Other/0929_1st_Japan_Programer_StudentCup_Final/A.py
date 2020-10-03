from itertools import (
    accumulate,  # 累積和のイテレータ
    groupby,  # 値をkey,同じ値の集まりをgroup
    permutations,  # 順列
    combinations,  # 組み合わせ
    product,  # 重複あり順列（直積, 深いネストにも使える）
    combinations_with_replacement,  # 重複あり組み合わせ
)

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

buf = [[] for _ in range(2*(10**6))]

for i, j in product(range(N), range(M)):
    tmp = A[i] + B[j]
    if not buf[tmp]:
        buf[tmp].extend([i, j])
    else:
        print(*buf[tmp], end=' ')
        print(i, j)
        exit()

print(-1)