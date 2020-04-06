n = int(input())

if n==1:
    print(1)
    exit()
else:
    ans = 1
    while ans<=n:
        ans *= 2

print(ans//2)