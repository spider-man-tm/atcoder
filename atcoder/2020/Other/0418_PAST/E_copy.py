N = int(input())
A = list(map(int, input().split()))

def func(x, target, iter):
    x = A[x-1]
    if x==target+1:
        return iter
    else:
        return func(x, target, iter+1)

for i in range(N):
    print(func(i+1, i, 1), end=' ')

print()