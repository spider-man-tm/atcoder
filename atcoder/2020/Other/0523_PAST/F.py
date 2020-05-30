from collections import deque

N = int(input())
a = [input() for _ in range(N)]

if N%2==0:
    word = deque([])
    for i in range(N//2):
        left = list(a[N//2-(i+1)])
        right = list(a[N//2+i])
        flag = False
        for v in left:
            if v in right:
                word.append(v)
                word.appendleft(v)
                flag = True
                break
        if flag==False:
            print(-1)
            exit()
    print(''.join(word))

else:
    tmp = a[N//2][0]
    word = deque([tmp])
    for i in range(N//2):
        left = list(a[N//2-(i+1)])
        right = list(a[N//2+(i+1)])
        flag = False
        for v in left:
            if v in right:
                word.append(v)
                word.appendleft(v)
                flag = True
                break
        if flag==False:
            print(-1)
            exit()
    print(''.join(word))