h = int(input())
hh = h
kaisuu = 0
while h>1:
    h //= 2
    kaisuu += 1

if hh==1:
    print(1)
else:
    ans = 1
    for i in range(1, kaisuu+1):
        ans += 2**i
    print(ans)