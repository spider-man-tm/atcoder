N, M = map(int, input().split())
box_num = [1]*N
box_color = [0]*N
box_color[0] = 1   # 0:白 1:赤 2:白or赤

for _ in range(M):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    box_num[x] -= 1
    box_num[y] += 1

    if box_num[y] != 1:
        if box_color[x]==box_color[y]:
            pass
        else:
            box_color[y] = 2
    else:
        box_color[y] = box_color[x]

ans = 0
for n, c in zip(box_num, box_color):
    if n>0:
        if c != 0:
            ans += 1

print(ans)