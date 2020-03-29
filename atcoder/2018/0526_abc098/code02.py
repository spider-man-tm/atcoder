n = int(input())
s = list(input())

maxi = 0

for i in range(n-1):
    left = set(s[:i+1])
    right = set(s[i+1:])
    g = len(left & right)
    if maxi<g:
        maxi = g

print(maxi)