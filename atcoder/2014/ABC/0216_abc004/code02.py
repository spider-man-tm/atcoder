C = []
for _ in range(4):
    a, b, c, d = input().split()
    C.append([a, b, c, d])

for i in range(4):
    for j in range(4):
        print(C[3-i][3-j], end=' ')
        if j==3:
            print()