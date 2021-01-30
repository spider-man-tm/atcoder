N, C = map(int, input().split())
event = []

for _ in range(N):
    a, b, c = map(int, input().split())
    a -= 1
    event.append((a, c))
    event.append((b, -c))

event = sorted(event)
ans, fee, time = 0, 0, 0

for x, y in event:
    if x != time:
        ans += min(C, fee) * (x - time)
        time = x
    fee += y

print(ans)