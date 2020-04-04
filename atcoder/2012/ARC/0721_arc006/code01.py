E = list(map(int, input().split()))
B = int(input())
L = list(map(int, input().split()))

cnt = len(set(E) & set(L))
bor = len({B} & set(L))

if cnt==6:
    print(1)
elif cnt==5 and bor==1:
    print(2)
elif cnt==5:
    print(3)
elif cnt==4:
    print(4)
elif cnt==3:
    print(5)
else:
    print(0)