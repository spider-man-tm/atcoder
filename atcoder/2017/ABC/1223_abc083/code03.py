X, Y = map(int, input().split())
ans = 0
a = X

while a<=Y:
    a *= 2
    ans += 1

print(ans)