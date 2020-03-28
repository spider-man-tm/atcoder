from collections import deque

S = deque(input())
Q = int(input())
SWITCH = False

for i in range(Q):
    v = list(input().split())
    if v[0] == '1':
        SWITCH = not SWITCH

    else:
        if v[1] == '1':
            if SWITCH==False:
                S.appendleft(v[2])
            else:
                S.append(v[2])
        else:
            if SWITCH==False:
                S.append(v[2])
            else:
                S.appendleft(v[2])

S = ''.join(S)

if SWITCH:
    print(S[::-1])
else:
    print(S)