N, K = map(int, input().split())

if K%2==1:
    print((N//K)**3)
else:
    a1 = N//K
    a2 = (N//(K//2)) - a1
    print(a1**3 + a2**3)