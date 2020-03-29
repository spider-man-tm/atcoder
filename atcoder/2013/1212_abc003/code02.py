s = input()
t = input()
ans = True
atcoder = ['a', 't', 'c', 'o', 'd', 'e', 'r']

for i, j in zip(s, t):
    if i != j:
        if i == '@':
            if j not in atcoder:
                ans = False
                break

        elif j == '@':
            if i not in atcoder:
                ans = False
                break

        else:
            ans = False
            break

if ans:
    print('You can win')
else:
    print('You will lose')