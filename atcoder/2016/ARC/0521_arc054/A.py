L, X, Y, S, D = map(int, input().split())

if S>D:
    t1 = (L-S+D)/(Y+X)
    if X==Y:
        print(t1)
        exit()
    t2 = (S-D)/(Y-X)
    t2 = t2 if t2>0 else float('inf')
    print(min(t1, t2))

else:
    t1 = (D-S)/(Y+X)
    if X==Y:
        print(t1)
        exit()
    t2 = (S+L-D)/(Y-X)
    t2 = t2 if t2>0 else float('inf')
    print(min(t1, t2))