S = input()
win = 0
for c in S:
    if c == 'o':
        win += 1

if win + (15 - len(S)) < 8:
    print('NO')
else:
    print('YES')