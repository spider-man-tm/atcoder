import itertools, math

def dist(way, n):
    dist = 0
    for i in range(n-1):
        x = (way[i][0] - way[i+1][0]) ** 2
        y = (way[i][1] - way[i+1][1]) ** 2
        dist += math.sqrt(x+y)
    return dist

n = int(input())
point = []

for _ in range(n):
    point.append(list(map(int, input().split())))

mean_dist = 0
cnt = 0
for v in itertools.permutations(point, n):
    mean_dist += dist(v, n)
    cnt += 1

print(mean_dist/cnt)