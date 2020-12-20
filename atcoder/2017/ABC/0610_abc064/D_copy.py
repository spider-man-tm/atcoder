N = int(input())
S = input()

l, r = 0, 0
for c in S:
    if c == '(':
        r += 1
    elif r:
        r -= 1
    else:
        l += 1

ans = '(' * l + S + ')' * r
print(ans)