from fractions import gcd

N, M = map(int, input().split())
A = list(map(int, input().split()))
flag = False
n = 1

# 全てを2で割る
for i in range(N):
    A[i] //= 2

for i in range(N):
    n *= A[i]//gcd(n, A[i])
    # 最小公倍数がMより大きくなる場合
    if n>M:
        flag = True
        break

for i in range(N):
    if (n//A[i])%2==0:
        flag = True
        break

if flag==False and M>=n:
    ans = 1
    M -= n
    ans += M//(2*n)
    print(ans)
else:
    print(0)