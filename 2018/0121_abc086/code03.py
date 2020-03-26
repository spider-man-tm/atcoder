n = int(input())
p = [0, 0]
time = 0

for _ in range(n):
    t, x, y = map(int, input().split())
    dist = abs(x-p[0]) + abs(y-p[1])
    if dist > t-time:
        print('No')
        exit()
    else:
        if (t-time)%dist==0:
            time += dist
            p = [x, y]
        else:
            print('No')
            exit()

print('Yes')