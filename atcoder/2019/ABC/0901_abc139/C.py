n = int(input())
h = list(map(int, input().split()))

steps = []
step = 0
before = -1

for i in h:
    if i <= before:
        step += 1
        before = i
    else:
        step = 0
        before = i
    steps.append(step)

print(max(steps))