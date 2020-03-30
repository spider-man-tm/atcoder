from collections import Counter
#l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']
#c = Counter(l)
#print(c)   # Counter({'a': 4, 'c': 2, 'b': 1})

N = int(input())
a = list(map(int, input().split()))

C = Counter(a)

ans = 0
for k, v in C.items():
    k = int(k)
    
    if k<v:
        ans += (v-k)
    elif k>v:
        ans += v

print(ans)