h, a = map(int, input().split())

if h%a==0:
    ans = h//a
else:
    ans = h//a + 1

print(ans)