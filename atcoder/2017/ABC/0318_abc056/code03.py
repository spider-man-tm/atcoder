x = int(input())

cnt = 0
for i in range(1, 10**10):
    cnt += i
    if x <= cnt:
        print(i)
        exit()