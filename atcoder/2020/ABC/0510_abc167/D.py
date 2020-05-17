import sys
sys.setrecursionlimit(10**9)

N, K = map(int, input().split())
A = list(map(int, input().split()))

log = []
check = [False]*N

def func(x, iter):
    x = A[x-1]

    if iter+1 == K:
        return x
    if check[x-1]:
        ix = log.index(x)
        loop = log[ix:]
        tmp = (K-iter-1)%len(loop)
        return loop[tmp]
    else:
        log.append(x)
        check[x-1] = True
        iter += 1
        return func(x, iter)

print(func(1, 0))