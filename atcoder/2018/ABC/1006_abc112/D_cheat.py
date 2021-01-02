def make_divisors(n):
    """
    約数の高速列挙
    """
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


N, M = map(int, input().split())

k = make_divisors(M)
k = sorted(k, reverse=True)
for i in k:
    if i * N <= M:
        print(i)
        exit()