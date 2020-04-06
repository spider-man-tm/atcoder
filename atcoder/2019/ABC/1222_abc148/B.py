n = input()
st = input().split()

ans = []
for i, j in zip(st[0], st[1]):
    ans.append(i)
    ans.append(j)

ans = ''.join(ans)
print(ans)