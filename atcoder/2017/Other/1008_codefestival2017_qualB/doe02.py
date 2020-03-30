from collections import Counter

N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

d = Counter(D)
t = Counter(T)

for k, v in t.items():
    if k not in d  or d[k]<v:
        print('NO')
        exit()

print('YES')