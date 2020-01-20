a, b = map(int, input().split())

fi = str(a)*b
se = str(b)*a

num = max(a, b)

for i in range(num):
    ff = int(fi[i])
    ss = int(se[i])
    if ff<ss:
        print(fi)
        break
    elif ss<ff:
        print(se)
        break
    else:
        pass

    if i==num-1:
        print(fi)