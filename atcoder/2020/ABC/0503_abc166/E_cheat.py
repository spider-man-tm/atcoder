from collections import Counter

N = int(input())
A = list(map(int, input().split()))

r = [(i+1)+a_i for i, a_i in enumerate(A)]
l = [(j+1)-a_j for j, a_j in enumerate(A)]
nr = Counter(r)
nl = Counter(l)

ans = 0
for k, v in nl.items():
    ans += nr[k]*v

print(ans)