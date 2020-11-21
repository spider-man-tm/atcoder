from math import ceil, sqrt

S, P = map(int, input().split())

for i in range(1, ceil(sqrt(P))+1):
    if P % i == 0:
        N = i
        M = P // i

        if N + M == S:
            print('Yes')
            exit()

print('No')