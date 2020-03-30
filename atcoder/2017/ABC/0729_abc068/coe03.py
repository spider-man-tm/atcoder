n, m = map(int, input().split())
start, end = [], []
for _ in range(m):
    t1, t2 = map(int, input().split())
    if t1==1:
        start.append(t2)
    if t2==n:
        end.append(t1)

start, end = set(start), set(end)
if len(start)+len(end)==len(start | end):
    print('IMPOSSIBLE')
else:
    print('POSSIBLE')