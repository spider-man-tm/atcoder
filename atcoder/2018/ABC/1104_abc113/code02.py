n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))

mini = float('inf')
ans = 0

for i in range(n):
    temp = t - h[i]*0.006
    diff = abs(a-temp)
    if diff < mini:
        mini = diff
        ans = i+1

print(ans)