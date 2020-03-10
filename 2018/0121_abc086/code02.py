a, b = input().split()
n = a+b
n = int(n)

ans = 'No'
for i in range(1, 1000):
    if n == (i**2):
        ans = 'Yes'

print(ans)