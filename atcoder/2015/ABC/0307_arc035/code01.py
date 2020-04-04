s = input()

def kaibun(s):
    n_iter = len(s)//2
    ans = True
    for i in range(n_iter):
        if s[i] != s[-1-i]:
            if s[i]!='*' and s[-1-i]!='*':
                ans = False
                break
    return ans

ans = 'YES' if kaibun(s) else 'NO'
print(ans)