from math import gcd


def factorization(n):
    arr, temp = [], n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr


A, B = map(int, input().split())
n_gcd = gcd(A, B)

fac = factorization(n_gcd)
ans = 0
if fac[0][0] != 1:
    ans += 1

ans += len(fac)
print(ans)