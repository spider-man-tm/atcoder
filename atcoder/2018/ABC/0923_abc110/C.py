S = list(input())
T = list(input())

dic1 = {}
dic2 = {}

for i in range(len(T)):
    tmp1 = T[i]
    tmp2 = S[i]
    if tmp1 not in dic1:
        dic1[tmp1] = tmp2
    else:
        if dic1[tmp1] != tmp2:
            print('No')
            exit()

    if tmp2 not in dic2:
        dic2[tmp2] = tmp1
    else:
        if dic2[tmp2] != tmp1:
            print('No')
            exit()

print('Yes')