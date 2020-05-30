N, L = map(int, input().split())
x = list(map(int, input().split()))
T1, T2, T3 = map(int, input().split())

p = 0
time = 0
while (p+4)<L:
    # 全部歩く
    t1 = 4*T1
    print('t1:',t1)
    if p+1 in x:
        t1 += T3
        print('t1:',t1)
    if p+2 in x:
        t1 += T3
        print('t1:',t1)
    if p+3 in x:
        t1 += T3
        print('t1:',t1)
    if p+4 in x:
        t1 += T3
    print('t1:',t1)

    # 前半歩いて後半行動2
    t2 = 3*T1+T2
    if p+1 in x:
        t2 += T3
    if p+2 in x:
        t2 += T3
    if p+4 in x:
        t2 += T3
    print('t2:',t2)

    # 前半行動2で後半歩く
    t3 = 3*T1+T2
    if p+2 in x:
        t3 += T3
    if p+3 in x:
        t3 += T3
    if p+4 in x:
        t3 += T3
    print('t3:',t3)

    # 中盤に行動2
    t4 = 3*T1+T2
    if p+1 in x:
        t4 += T3
    if p+3 in x:
        t4 += T3
    if p+4 in x:
        t4 += T3
    print('t4:',t4)

    # 行動3
    t5 = T1+T2*3
    if p+4 in x:
        t5 += T3
    print('t5:',t5)

    time += min(t1,t2,t3,t4,t5)
    p += 4

    print(t1,t2,t3,t4,t5)

print(time)
print(p)