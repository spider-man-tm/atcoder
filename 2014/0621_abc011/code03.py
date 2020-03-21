n = int(input())
ng1 = int(input())
ng2 = int(input())
ng3 = int(input())
ng_list = [ng1, ng2, ng3]

if n in ng_list:
    print('NO')
    exit()

for _ in range(100):
    if n-3 not in ng_list:
        n -= 3
    elif n-2 not in ng_list:
        n -= 2
    elif n-1 not in ng_list:
        n -= 1
    else:
        print('NO')
        exit()

    if n<=0:
        print('YES')
        exit()

print('NO')