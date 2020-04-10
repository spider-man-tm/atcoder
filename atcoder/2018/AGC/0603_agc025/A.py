N = int(input())

def digsum(n):
    total = 0
    while n > 0:
        total += n%10
        n /= 10
        n = int(n)
    return total

ans = float('inf')
for i in range(2, N//2+2):
    A = i
    B = N-A
    s = digsum(A)+digsum(B)
    ans = min(ans, s)

print(ans)