C = [input() for _ in range(2)]

for i in range(2):
    for j in range(3):
        if C[i][j] != C[1-i][2-j]:
            print('NO')
            exit()

print('YES')