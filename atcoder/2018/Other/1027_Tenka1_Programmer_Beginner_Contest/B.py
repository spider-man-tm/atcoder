A, B, K = map(int, input().split())

for i in range(K):
    if i%2==0:
        if A%2==1:
            A -= 1
        tmp = A//2
        A //= 2
        B += tmp
    else:
        if B%2==1:
            B -= 1
        tmp = B//2
        B //= 2
        A += tmp

print(A, B)