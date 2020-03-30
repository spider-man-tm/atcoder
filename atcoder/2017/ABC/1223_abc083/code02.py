N, A, B = map(int, input().split())

def digsum(n):
    total = 0
    while n > 0:
        total += n%10
        n /= 10
        n = int(n)
    return total

ans = 0
for i in range(1, N+1):
    if A <= digsum(i) <= B:
        ans += i

print(ans)