N = int(input())

def F(a, b):
    return max( len(str(a)), len(str(b)) )

ans = float('inf')
n_iter = int(N**(1/2))+1

for i in range(1, n_iter):
    if N%i==0:
        ans = min( ans, F(i, N//i) )

print(ans)