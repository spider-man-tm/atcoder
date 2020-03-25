a, b = map(int, input().split())
diff = abs(a-b)
ans = 0

while diff>0:
    if diff>=7.5:
        diff -= 10
        diff = abs(diff)
        ans += 1
    elif diff>=3:
        diff -= 5
        diff = abs(diff)
        ans += 1
    else:
        diff -= 1
        ans += 1

print(ans)