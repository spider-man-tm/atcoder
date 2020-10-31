X, Y, A, B = map(int, input().split())

ans = 0
while X*A <= X+B and A*X < Y:
    X *= A
    ans += 1

print(ans + (Y-1+X) // B)