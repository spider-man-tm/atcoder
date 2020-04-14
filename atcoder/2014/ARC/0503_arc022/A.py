S = input().lower()
w = ''

for c in S:
    if w == '':
        if c == 'i':
            w += c
    elif w == 'i':
        if c == 'c':
            w += 'c'
    elif w == 'ic':
        if c == 't':
            w += 't'
            break

if w == 'ict':
    print('YES')
else:
    print('NO')