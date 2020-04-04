w, h, x, y = map(int, input().split())
center = (w/2, h/2)
ans2 = 1 if (x, y)==center else 0
ans1 = w*h/2
print(ans1, ans2)