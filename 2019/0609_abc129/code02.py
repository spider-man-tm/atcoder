n = int(input())
w = list(map(int, input().split()))

best = 10000000000000

total = sum(w)
for i in range(len(w)):
    su = sum(w[:i])
    diff = abs(su - (total-su))
    if diff < best:
        best = diff

print(best)