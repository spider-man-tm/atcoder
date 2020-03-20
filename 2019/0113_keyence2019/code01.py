n1, n2, n3, n4 = map(int, input().split())
ans = sorted(list({n1, n2, n3, n4}))
if ans == [1, 4, 7, 9]:
    print('YES')
else:
    print('NO')