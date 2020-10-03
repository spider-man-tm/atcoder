H, W, M = map(int, input().split())
bom = set()
row = [0] * H
col = [0] * W

for _ in range(M):
    h, w = map(int, input().split())
    bom.add((h-1, w-1))
    row[h-1] += 1
    col[w-1] += 1

max_row = max(row)
max_col = max(col)
ans = max_row + max_col - 1

p, q = [], []

for i in range(H):
    if row[i] == max_row:
        p.append(i)

for j in range(W):
    if col[j] == max_col:
        q.append(j)

flag = False
for i in p:
    for j in q:
        if (i, j) not in bom:
            ans += 1
            flag = True
            break
    if flag:
        break

print(ans)
