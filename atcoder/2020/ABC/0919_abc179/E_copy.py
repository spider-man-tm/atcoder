n, x, m = map(int, input().split())
ans = x
L = [0 for i in range(m+1)]
L[x] = 1

A = [x]
t = True
count = 2
while t:
    x = (x*x)%m
    if L[x] != 0:
        start = L[x]
        t = False
    else:
        L[x] = count
        count += 1
        A.append(x)

if A[-1] == 0:
    if len(A) - 1 > n:
        ans = sum(A[:n])
    else:
        ans = sum(A)

elif len(A) >= n:
    ans = sum(A[:n])
else:
    length = len(A)-start+1
    ans = sum(A[:(start-1)])
    t = (n-start+1) // length 
    s = (n-start+1) % length
    ans += sum(A[(start-1):])*t 
    ans += sum(A[start-1:(start-1+s)])
print(ans)
