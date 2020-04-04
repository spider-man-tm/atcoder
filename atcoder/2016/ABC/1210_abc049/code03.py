S = input()
S = ''.join(list(reversed([c for c in S])))

while S:
    if S[:7] == 'remaerd':
        S = S[7:]
    elif S[:6] == 'resare':
        S = S[6:]
    elif S[:5] == 'maerd':
        S = S[5:]
    elif S[:5] == 'esare':
        S = S[5:]
    else:
        print('NO')
        exit()

print('YES')