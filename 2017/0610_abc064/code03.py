n = int(input())
a = list(map(int, input().split()))

rate_list = [0, 0, 0, 0, 0, 0, 0, 0]
perfect = 0

for i in range(n):
    rate = a[i]//400
    if rate < 8:
        if rate_list[rate] == 0:
            rate_list[rate] += 1
    else:
        perfect += 1
        
mini = max(sum(rate_list), 1)
maxi = sum(rate_list)+perfect

print(mini, maxi)