a = int(input())
b = int(input())

print(a, b)

ans = [c for c in range(1, 4) if c not in [a, b]]

for i in ans:
    print(i)