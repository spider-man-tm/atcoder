N = int(input())
A = list(map(int, input().split()))

S = set()
for a in A:
    # 奇数になるまで割り続ける
    while a%2==0:
        a //= 2
    S.add(a)

print(len(S))