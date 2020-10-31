T = int(input())
MOD = 10 ** 9 + 7

def check(n, a, b):
    if a + b > n:
        return 0

    blue = (n - a + 1) ** 2 % MOD
    red = (n - b + 1) ** 2 % MOD
    ans = blue * red % MOD
    
    X4 = (n - a - b + 2) * (n - a - b + 1) // 2
    X3 = 2 * X4
    X2 = (n - a + 1) * (n - b + 1) - X3
    X1 = X2 ** 2 % MOD
    ans -= X1
    ans %= MOD
    
    return ans

for _ in range(T):
    N, A, B = map(int, input().split())
    print(check(N, A, B))
