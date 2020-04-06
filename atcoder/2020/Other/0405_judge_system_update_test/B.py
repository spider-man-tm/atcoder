N = int(input())
XC = [list(input().split()) for _ in range(N)]
B, R = [], []

for x, c in XC:
    if c=='R':
        R.append(int(x))
    else:
        B.append(int(x))

B = sorted(B)
R = sorted(R)

ans = R+B
for i in ans:
    print(i)