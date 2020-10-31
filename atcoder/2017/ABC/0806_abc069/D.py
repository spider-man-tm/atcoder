def color_print(tile):
    for l in tile:
        print(*l)

H, W = map(int, input().split())
N = int(input())
a = list(map(int, input().split()))

color = []
cnt = 1
for i in range(N):
    color.extend([cnt]*a[i])
    cnt += 1


ans = [[0]*W for _ in range(H)]
cnt = 0
for i in range(H):
    for j in range(W):
        if i % 2 == 1:
            j = W - j - 1

        ans[i][j] = color[cnt]
        cnt += 1
 
color_print(ans)