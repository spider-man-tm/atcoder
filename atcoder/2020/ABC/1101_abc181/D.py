from collections import Counter

S = input()
N = int(S)
C = Counter(S)

if len(S) < 2:
    if N == 8:
        print('Yes')
    else:
        print('No')

elif len(S) < 3:
    if N % 8 == 0:
        print('Yes')
    elif int(S[::-1]) % 8 == 0:
        print('Yes')
    else:
        print('No')

else:
    hachi = []
    i = 104
    while i < 1000:
        hachi.append(i)
        i += 8

    for i in hachi:
        flag = True
        i = str(i)
        c = Counter(i)
        for k, v in c.items():
            if C[k] < v:
                flag = False
        if flag:
            print('Yes')
            exit()

    print('No')
