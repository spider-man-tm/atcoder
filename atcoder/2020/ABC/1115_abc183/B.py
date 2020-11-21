Sx, Sy, Gx, Gy, = map(int, input().split())

tmp = Sy / (Sy + Gy)
dx = abs(Gx - Sx)

ans1 = Sx + tmp*dx
ans2 = Sx - tmp*dx

if Gx>=Sx:
    print(ans1)
else:
    print(ans2)