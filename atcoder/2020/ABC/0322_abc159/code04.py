from collections import Counter

n = int(input())
a = list(map(int, input().split()))
re = [0] * (n+1)

c = Counter(a)   # c: Counter({1: 3, 2: 2})など
for k, v in c.items():
    re[k] = v*(v-1) // 2

total = sum(re)
for i in a:
    print(total - re[i] + (c[i]-1)*(c[i]-2) // 2)