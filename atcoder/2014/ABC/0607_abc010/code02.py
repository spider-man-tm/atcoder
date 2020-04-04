n = int(input())
a = list(map(int, input().split()))
ans = 0

for i in range(n):
    num = a[i]
    while num%2==0 or num%3==2:
        num -= 1
        ans += 1
    
print(ans)