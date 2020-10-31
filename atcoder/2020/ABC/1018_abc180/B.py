N = int(input())
x = list(map(int, input().split()))

ans1, ans2, ans3 = 0, 0, 0

for xx in x:
    ans1 += abs(xx)
    ans2 += int(xx**2)
    ans3 = max(ans3, abs(xx))

ans2 **= (1/2)

print(ans1)
print(ans2)
print(ans3)