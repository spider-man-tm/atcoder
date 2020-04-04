t = int(input())
_ = int(input())
a = list(map(int, input().split()))
_ = int(input())
b = list(map(int, input().split()))

for i in range(len(b)):
    flag = False
    for j in range(len(a)):
        if 0 <= b[i] - a[j] <= t:
            a.pop(j)
            flag = True
            break

    if flag==False:
        print('no')
        exit()

print('yes')