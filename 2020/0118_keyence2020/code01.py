h = int(input())
w = int(input())
n = int(input())

total = h*w
kesu = max(h, w)

if n%kesu==0:
    print(n//kesu)
else:
    print(n // kesu + 1)