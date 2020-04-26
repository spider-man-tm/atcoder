s = list(input())

def check(c):
    if c not in s:
        return float('inf')

    cnt = 0
    ans = 0
    for i in s:
        if i==c:
            cnt = 0
        else:
            cnt += 1
        ans = max(ans, cnt)
    return ans

ans = float('inf')
for i in range(97, 97+26):
    c = chr((i))
    ans = min(ans, check(c))

print(ans)