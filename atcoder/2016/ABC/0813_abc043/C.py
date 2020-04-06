N = int(input())
a = list(map(int, input().split()))

mean = round(sum(a)/len(a))
ans = 0
for i in range(N):
    ans += (a[i]-mean)**2

print(ans)