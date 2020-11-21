A, B, C = map(int, input().split())
mod = 998244353

def sums(x):
    return (1+x)*x // 2 % mod

sumA, sumB, sumC = sums(A), sums(B), sums(C)
ans = (sumA * sumB * sumC) % mod
print(ans)