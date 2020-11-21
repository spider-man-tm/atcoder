from itertools import (
    accumulate,  # 累積和のイテレータ
    groupby,  # 値をkey,同じ値の集まりをgroup
    permutations,  # 順列
    combinations,  # 組み合わせ
    product,  # 重複あり順列（直積, 深いネストにも使える）
    combinations_with_replacement,  # 重複あり組み合わせ
)

N, K = map(int, input().split())
T = []
for _ in range(N):
    T.append(list(map(int, input().split())))

cnt = 0
for v in permutations(range(N-1), N-1):
    now, time = 0, 0
    for i in v:
        i += 1
        time += T[now][i]
        now = i
    time += T[now][0]
    if time == K:
        cnt +=1

print(cnt)