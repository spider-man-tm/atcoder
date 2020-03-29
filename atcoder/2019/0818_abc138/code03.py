n = int(input())
v = sorted(list(map(int, input().split())))

while len(v)>1:
    g1, g2 = v[0], v[1]
    g = (g1+g2)/2
    v = [g]+ v[2:]
    v = sorted(v)

print(v[0])