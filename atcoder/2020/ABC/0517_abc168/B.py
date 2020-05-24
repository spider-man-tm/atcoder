K = int(input())
S = input()

if len(S)<=K:
    print(S)
else:
    ans = S[:K] + '...'
    print(ans)