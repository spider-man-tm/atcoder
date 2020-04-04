A, B, C = map(int, input().split())

if A==B==C and A%2==0:
    print(-1)
    exit()

ans = 0
while A%2==0 and B%2==0 and C%2==0:
    tmpA = A//2
    tmpB = B//2
    tmpC = C//2
    A = tmpB+tmpC
    B = tmpC+tmpA
    C = tmpA+tmpB
    ans += 1

print(ans)