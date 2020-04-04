A, B, X = map(int,input().split())

def check(N,X):
    return A*N + B*len(str(N)) <= X

left = 0
right = 10**9+1			
while right - left > 1:
    mid = (right + left)//2
    print(left, right)
    if check(mid, X):
        left = mid
    else:
        right = mid

print(left)