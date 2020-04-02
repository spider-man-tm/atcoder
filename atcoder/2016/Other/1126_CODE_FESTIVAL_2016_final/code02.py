N = int(input())

total = 0
x = 0
for i in range(1, N+1):
    total += i
    x = i
    if total >= N:
        break

diff = total-N
for i in range(1, x+1):
    if i!=diff:
        print(i)