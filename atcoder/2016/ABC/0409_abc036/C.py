from bisect import bisect_left, bisect_right  # return index

def search(t, i):
    '''存在するかどうかを返す'''
    ix = bisect_right(t, i)
    if t[ix-1] != i:
        return False
    return True

N = int(input())
A = [int(input()) for _ in range(N)]

AA = list(set(A))
AA = sorted(AA)

for i in A:
    print(bisect_left(AA, i))