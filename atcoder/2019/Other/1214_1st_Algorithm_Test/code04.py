N = int(input())

dic = {i: 0 for i in range(1, N+1)}
for _ in range(N):
    i = int(input())
    dic[i] += 1

ans = True
for k, v in dic.items():
    if v!=1:
        ans = False
        if v==0:
            x = k
        else:
            y = k

if ans:
    print('Correct')
else:
    print(y, x)