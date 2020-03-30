n = int(input())
a = list(map(int, input().split()))
a = [0] + a + [0]
cost = [abs(a[i+1]-a[i]) for i in range(n+1)]
total = sum(cost)

#print('a: ', a)
#print('cost: ', cost)

for i in range(n):
    ans = total-cost[i]-cost[i+1]
    ans += abs(a[i]-a[i+2])
    print(ans)