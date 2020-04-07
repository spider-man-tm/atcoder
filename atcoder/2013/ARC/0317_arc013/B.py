C = int(input())

a1, a2, a3 = 0, 0, 0

for _ in range(C):
    box = sorted(list(map(int, input().split())))
    a1 = max(a1, box[0])
    a2 = max(a2, box[1])
    a3 = max(a3, box[2])

print(a1*a2*a3)