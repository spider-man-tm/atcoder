N, L = map(int, input().split())
amida = [' ' + input() + ' ' for _ in range(L+1)]

for j in range(N):
    now = j*2+1
    for i in range(L):
        if amida[i][now-1] == '-':
            now -= 2
        elif amida[i][now+1] == '-':
            now += 2
            
    if amida[i+1][now] == 'o':
        print(j+1)
        break