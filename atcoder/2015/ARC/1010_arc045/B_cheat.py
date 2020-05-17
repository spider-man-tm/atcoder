def get_line_formula(x1, y1, x2, y2):
    """
    (x1, y1)と(x2, y2)の2点を通過する直線の式
    a*x + b*y +c = 0
    return a, b, c
    """
    # x軸と並行
    if y1==y2:
        return 0, 1, -y1
    # y軸と並行
    elif x1==x2:
        return 1, 0, -x1
    else:
        a = (-(y1 - y2)) / (x1 - x2)
        b = 1
        c = - (a * x1) - y1
        return a, b, c


def get_point_line_distance(x, y, a, b, c):
    """
    直線: a*x + b*y + c = 0
    点: x, y
    の距離を返す
    """
    return abs(a*x + b*y + c) / ((a**2 + b**2) ** 0.5)


x, y = map(int, input().split())
N = int(input())
P = []

for _ in range(N):
    P.append(list(map(int, input().split())))
P.append(P[0])

ans = float('inf')
for i in range(N):
    a0, b0 = P[i]
    a1, b1 = P[i+1]
    a, b, c = get_line_formula(a0, b0, a1, b1)
    dist = get_point_line_distance(x, y, a, b, c)
    ans = min(ans, dist)

print(ans)