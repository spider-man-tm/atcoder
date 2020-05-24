def kaibun(s):
    n_iter = len(s)//2
    ans = True
    for i in range(n_iter):
        if s[i] != s[-1-i]:
            ans = False
            break
    return ans


S = input()

if kaibun(S):
    print('YES')
else:
    print('NO')