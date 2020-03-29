n = int(input())
c = input()
ans = [0, 0, 0, 0]
for i in c:
    i = int(i)-1
    ans[i] += 1

print(max(ans), min(ans))