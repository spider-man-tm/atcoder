def helper(v):
    for i in range(len(v)):
        print(*v[i])

def helper2(v, i, j, H, W):
    v = [v[i][j:j+W] for i in range(i, i+H)]
    helper(v)

def rotate(v, k=1):
    import numpy as np
    v2 = np.array(v)
    v2 = np.rot90(v, k)
    v2 = list(v2)
    return v2


H, W = map(int, input().split())
Dai, Stamp = [], []
for i in range(H):
    Dai.append('$'*10 + input() + '$'*10)
for i in range(H):
    Stamp.append(list(input()))
tmp = ['$' * (20 + W) for _ in range(10)]
Dai = tmp + Dai + tmp
Stamp0 = rotate(Stamp, 0)
Stamp1 = rotate(Stamp, 1)
Stamp2 = rotate(Stamp, 2)
Stamp3 = rotate(Stamp, 3)

def func(Stamp, Dai):
    for i in range(len(Dai)-len(Stamp)):
        for j in range(len(Dai[0])-len(Stamp[0])):
            stop = False

            for ii in range(len(Stamp)):
                if stop:
                    break

                for jj in range(len(Stamp[0])):
                    if Stamp[ii][jj] == '#':
                        if Dai[i+ii][j+jj] == '#' or Dai[i+ii][j+jj] == '$':
                            stop = True
                            break
            
            if not stop:
                '''
                print()
                print('Stamp')
                helper(Stamp)
                print('Dai')
                helper2(Dai, i, j, H, W)
                '''
                return 'Yes'
    return 'No'

ans = [func(Stamp0, Dai), func(Stamp1, Dai), func(Stamp2, Dai), func(Stamp3, Dai)]

if 'Yes' in ans:
    print('Yes')
else:
    print('No')
