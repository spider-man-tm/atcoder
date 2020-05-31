N = int(input())
d = []

for _ in range(N):
    d.append(int(input()))

if N==1:
    print(d[0])
    print(d[0])
    exit()

d = sorted(d)
maxi = sum(d)

if d[-1] > sum(d[:-1]):
    mini = d[-1] - sum(d[:-1])
else:
    mini = 0

print(maxi)
print(mini)