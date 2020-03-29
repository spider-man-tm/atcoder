n = int(input())
b = list(map(int, input().split()))
a = [0] * n
a[0] = b[0]

if n==2:
    print(b[0]*2)
    exit()

for i in range(1, n-1):
    a[i] = min(b[i], b[i-1])
    a[i+1] = b[i]

print(sum(a))