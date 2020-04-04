string = input()
ans = []

for s in string:
    if s=='0':
        ans.append('0')
    elif s=='1':
        ans.append('1')
    else:
        if len(ans) != 0:
            ans.pop()

for s in ans:
    print(s, end='')
print()