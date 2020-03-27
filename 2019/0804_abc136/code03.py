N = int(input())
H = list(map(int, input().split()))

before = H[0]
for i in range(1, N):
    h = H[i]
    if h > before:
        H[i] -= 1
    elif h < before:
        print('No')
        exit()
    
    before = H[i]

print('Yes')