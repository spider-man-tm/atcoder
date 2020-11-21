def counter(S, point):
    x, y = point
    cnt = 0
    cnt += S[x][y] == '#'
    cnt += S[x][y+1] == '#'
    cnt += S[x][y-1] == '#'
    cnt += S[x+1][y] == '#'
    cnt += S[x+1][y+1] == '#'
    cnt += S[x+1][y-1] == '#'
    cnt += S[x-1][y] == '#'
    cnt += S[x-1][y+1] == '#'
    cnt += S[x-1][y-1] == '#'
    return cnt

N, M = map(int, input().split())
s = ['.' * (M+2)]

for _ in range(N):
    tmp = input()
    tmp = '.' + tmp + '.'
    s.append(tmp)

s.append('.' * (M+2))

for i in range(1, N+1):
    for j in range(1, M+1):
        print(counter(s, [i, j]), end = '')
    print()