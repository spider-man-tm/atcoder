n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
manzoku = 0

for i in range(n):
    manzoku += b[a[i]-1]
    if i != 0:
        if (a[i]==a[i-1]+1):
            manzoku += c[a[i-1]-1]

print(manzoku)