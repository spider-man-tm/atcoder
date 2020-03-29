n = int(input())
a = list(map(int, input().split()))

a_i = max(a)
half = a_i/2

best = a_i*2
for j in a:
    if j==a_i:
        continue

    diff = abs(j-half)
    if diff < best:
        best = diff
        a_j = j

print(a_i, a_j)