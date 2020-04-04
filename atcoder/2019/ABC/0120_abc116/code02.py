s = int(input())

lis = []

flag = True
while flag:
    lis.append(s)
    if s%2==0:
        s /= 2
    else:
        s = s*3 + 1
    s = int(s)

    if s in lis:
        print(len(lis)+1)
        flag = False