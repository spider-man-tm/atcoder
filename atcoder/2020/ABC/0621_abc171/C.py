N = int(input())

ans = ''

while True:
    N -= 1
    N, mod = N//26, N%26
    ans += chr(ord('a') + mod)
    if N==0:
        break

print(ans[::-1])