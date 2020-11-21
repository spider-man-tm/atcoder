N, W = map(int, input().split())

time = [0] * (2*(10**5) + 100)
#time = [0] * 20

for _ in range(N):
    S, T, P = map(int, input().split())
    time[S] += P
    time[T] -= P

water = 0
for i in range(len(time)):
    water += time[i]
    if water > W:
        print('No')
        exit()

print('Yes')