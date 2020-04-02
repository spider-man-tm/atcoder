K = int(input())
a, b = 2, 1
for _ in range(K-1):
    a, b = a+b, a

print(a, b)