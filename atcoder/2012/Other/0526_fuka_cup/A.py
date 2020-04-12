while True:
    n, k = map(int, input().split())
    if n==0 and k==0:
        break
    X = sorted(list(map(int, input().split())))
    print(sum(X[:k]))