N = int(input())

for i in range(1000001):
    if i**2>N:
        break

print((i-1)**2)