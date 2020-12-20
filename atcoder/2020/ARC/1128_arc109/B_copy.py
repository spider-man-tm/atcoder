n = int(input())

l, r = 0, 10**18
while l + 1 < r:
    m = (l + r) // 2
    total = (1 + m) * (m // 2)
    if total > n + 1:
        r = m
    else:
        l = m

print(n + 1 - l)
