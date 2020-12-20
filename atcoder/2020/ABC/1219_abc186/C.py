N = int(input())

ans = 0

for i in range(1, N+1):
    flag = True
    dec = str(i)
    for s in dec:
        if s == '7':
            ans += 1
            flag = False
            break
    if flag:
        octi = oct(i)[2:]
        for s in octi:
            if s == '7':
                ans += 1
                break

print(N-ans)