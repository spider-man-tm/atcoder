C = [list(map(int, input().split())) for _ in range(3)]
ans = 'Yes'

for i in range(2):
    if C[i][0] - C[i+1][0] != C[i][1] - C[i+1][1] or \
        C[i][0] - C[i+1][0] != C[i][2] - C[i+1][2]:
        ans = 'No'

        
for j in range(2):
    if C[0][j] - C[0][j+1] != C[1][j] - C[1][j+1] or \
        C[0][j] - C[0][j+1] != C[2][j] - C[2][j+1]:
        ans = 'No'

print(ans)