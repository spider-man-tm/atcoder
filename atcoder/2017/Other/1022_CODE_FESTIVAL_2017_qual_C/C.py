s = input()

l, r = 0, len(s)-1
ans = 0
i = 0

while l<r:
    left = s[l]
    right = s[r]
    
    if left == right:
        l += 1
        r -= 1
    else:
        if left == 'x':
            l += 1
            ans += 1
        elif right == 'x':
            r -= 1
            ans += 1
        else:
            print(-1)
            exit()
    i += 1

print(ans)