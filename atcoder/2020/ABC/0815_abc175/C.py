X, K, D = map(int, input().split())

diff = abs(X)

if K * D <= diff:
    if X >= 0:
        print(X - D * K)
    else:
        print(-1 * (X + D * K))

else:
    mod = diff // D
    if X >= 0:
        plus = X - D * mod
        minus = plus - D
        if (K - mod) % 2 == 0:
            print(plus)
        else:
            print(-minus)
    else:
        minus = X + D * mod
        plus = minus + D
        if (K - mod) % 2 == 0:
            print(-minus)
        else:
            print(plus)