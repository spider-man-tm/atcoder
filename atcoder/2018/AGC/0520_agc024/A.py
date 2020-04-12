A, B, C, K = map(int, input().split())

if K%2==0:
    ans = A-B
    if ans >= 10**18:
        print('Unfair')
    else:
        print(ans)
else:
    ans = B-A
    if ans >= 10**18:
        print('Unfair')
    else:
        print(ans)