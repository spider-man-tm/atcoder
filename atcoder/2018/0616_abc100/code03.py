N = int(input())
a = list(map(int, input().split()))

def factorization(n):
    cnt = 0
    while n%2==0:
        n /= 2
        cnt += 1
    return cnt

fac = [0] * N
for i in range(N):
    if a[i]%2==0:
        fac[i] = factorization(a[i])

print(sum(fac))