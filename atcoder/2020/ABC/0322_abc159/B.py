s = input()

left = s[:len(s)//2]
right = s[len(s)//2+1:]

def kaibun(s):
    n_iter = len(s)//2
    ans = True
    for i in range(n_iter):
        if s[i] != s[-1-i]:
            ans = False
            break
    return ans


if kaibun(left)==True and kaibun(right)==True and kaibun(s)==True:
    print('Yes')
else:
    print('No')