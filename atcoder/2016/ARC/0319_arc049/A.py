from collections import deque

S = deque(list(input()))
A, B, C, D = map(int, input().split())

for i in range(len(S)+4):
    if i==A or i==B+1 or i==C+2 or i==D+3:
        print('"', end='')
    else:
        print(S.popleft(), end='')
print()