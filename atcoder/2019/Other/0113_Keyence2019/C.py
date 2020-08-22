import numpy as np
from bisect import bisect_left, bisect_right  # return index

N = int(input())
A = np.array(list(map(int, input().split())))
B = np.array(list(map(int, input().split())))

if A.sum() < B.sum():
    print(-1)
    exit()

diff = A - B
diff = np.sort(diff).tolist()

zero_ix = bisect_left(diff, 0)
plus = diff[zero_ix:][::-1]
minus = diff[:zero_ix]
minus_sum = sum(minus)

cnt = len(minus)
if cnt == 0:
    print(0)
    exit()

for i in range(len(plus)):
    cnt += 1
    minus_sum += plus[i]
    if minus_sum >= 0:
        break

print(cnt)
