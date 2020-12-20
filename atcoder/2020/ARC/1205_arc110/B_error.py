from math import ceil

N = int(input())
T = input()

if T[:3] == '110':
    for i in range(N):
        if i % 3 == 0:
            if T[i] != '1':
                print(0)
                exit()
        elif i % 3 == 1:
            if T[i] != '1':
                print(0)
                exit()
        else:
            if T[i] != '0':
                print(0)
                exit()
    last = ceil(N / 3)
    print(10**10 - last + 1)

elif T[:3] == '101':
    for i in range(N):
        if i % 3 == 0:
            if T[i] != '1':
                print(0)
                exit()
        elif i % 3 == 1:
            if T[i] != '0':
                print(0)
                exit()
        else:
            if T[i] != '1':
                print(0)
                exit()
    last = ceil((N+1) / 3)
    print(10**10 - last + 1)

elif T[:3] == '011':
    for i in range(N):
        if i % 3 == 0:
            if T[i] != '0':
                print(0)
                exit()
        elif i % 3 == 1:
            if T[i] != '1':
                print(0)
                exit()
        else:
            if T[i] != '1':
                print(0)
                exit()
    last = ceil((N+2) / 3)
    print(10**10 - last + 1)

else:
    print(0)