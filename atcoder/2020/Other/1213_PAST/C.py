N = int(input())
moji = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans = ''

while True:
    mod = N % 36
    N //= 36
    ans = moji[mod] + ans

    if N < 36:
        if N > 0:
            ans = moji[N] + ans
            break
        break

print(ans)