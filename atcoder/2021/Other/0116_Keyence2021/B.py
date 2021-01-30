from collections import Counter
#l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']
#c = Counter(l)
#print(c)   # Counter({'c': 2, 'a': 4, 'b': 1})  順番は適当
#c = Counter(l).most_common()
#print(c)   # [('a', 4), ('c', 2), ('b', 1)]

N, K = map(int, input().split())
a = list(map(int, input().split()))

c = Counter(a)

cnt = K
ans = 0
for i in range(N):
    if not c[i]:
        ans += K * i
        break
    else:
        if c[i] < K:
            ans += (K - c[i]) * i
            K = c[i]

print(ans)