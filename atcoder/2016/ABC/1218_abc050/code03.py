n = int(input())
a = list(map(int, input().split()))
dic = {}
mod = 10**9+7

if n%2==0:
    for i in a:
        if i%2==0:
            print(0)
            exit()
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    for k, v in dic.items():
        if v != 2:
            print(0)
            exit()
    print(2**(n//2)%mod)

else:
    for i in a:
        if i%2==1:
            print(0)
            exit()
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    for k, v in dic.items():
        if v != 2 and k != 0:
            print(0)
            exit()
    print(2**(n//2)%mod)