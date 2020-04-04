L, R = map(int, input().split())
l = list(map(int, input().split()))
r = list(map(int, input().split()))

pair = 0
for i in range(10, 41):
    ll = l.count(i)
    rr = r.count(i)
    pair += min(ll, rr)

print(pair)