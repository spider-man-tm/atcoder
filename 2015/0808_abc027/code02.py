n = int(input())
a = list(map(int, input().split()))

if sum(a)%n != 0:
    print(-1)
    exit()

per = sum(a)//n
ans = 0

for i in range(n):
    if a[i] != per:
        ans += 1
        tmp = a[i]
        a[i] = per
        a[i+1] += (tmp-per)
        
print(ans)