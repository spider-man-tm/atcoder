from math import ceil, floor

N = int(input())
T = input()

if N == 1:
    if T == '1':
        print(2*10**10)
    else:
        print(10**10)
    exit()


def check(t, p1, p2, p3):
    for i in range(len(t)):
        if i % 3 == 0:
            if t[i] != p1:
                return False
        elif i % 3 == 1:
            if t[i] != p2:
                return False
        else:
            if t[i] != p3:
                return False
    return True


def check2(t):
    if t[:2] == '11':
        if check(t, '1', '1', '0'):
            length = ceil(N / 3)
            print(10**10 - length + 1)
        else:
            print(0)
    elif t[:2] == '10':
        if check(t, '1', '0', '1'):
            length = ceil((N+1) / 3)
            print(10**10 - length + 1)
        else:
            print(0)
    elif t[:2] == '01':
        if check(t, '0', '1', '1'):
            length = ceil((N+2) / 3)
            print(10**10 - length + 1)
        else:
            print(0)
    else:
        print(0)

check2(T)
