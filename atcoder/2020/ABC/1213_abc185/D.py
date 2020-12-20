from math import ceil, floor
#ceil()  # 切り上げ。常にup
#floor()  # 切り捨て。常にdown
#int()  # 常に0に近く（正負で挙動違う）
#round(f),  round(f, 1)  # 四捨五入（第二引数で小数点桁数を指定）

N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
A.append(N+1)

if not M:
    print(1)
elif N == M:
    print(0)
else:
    now = 0
    k = N
    for i in range(M+1):
        white = A[i]-now-1
        if white:
            k = min(k, white)
        now = A[i]

    ans = 0
    now = 0
    for i in range(M+1):
        white = A[i]-now-1
        ans += ceil(white / k)
        now = A[i]

    print(ans)
