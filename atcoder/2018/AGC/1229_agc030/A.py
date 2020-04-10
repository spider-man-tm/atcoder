A, B, C = map(int, input().split())
ans = min(A+B+1, C) + B
print(ans)