x = int(input())
a = int(input())
b = int(input())

for i in range(1, 100000):
    total = a + b*i
    if total > x:
        break

print(x - (a + b*(i-1)))