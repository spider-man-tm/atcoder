n = int(input())
a = list(map(int, input().split()))

left = sum(a)
right = 0

mini = float('inf')
for i in a:
    right += i
    left -= i
    tmp = abs(right - left)

    if tmp < mini:
        mini = tmp

print(mini)