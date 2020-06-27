from collections import deque

s = deque(input())
t = deque(input())

ans = 0
flag = False
for _ in range(len(s)):
    if s == t:
        flag = True
        break
    else:
        tmp = s.pop()
        s.appendleft(tmp)
        ans += 1

if flag:
    print(ans)
else:
    print(-1)