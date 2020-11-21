from itertools import permutations

N = int(input())
S = input()

for v in permutations(range(N), N):
    tmp = ''
    for i in v:
        tmp += S[i]
    if tmp != S and tmp != S[::-1]:
        print(tmp)
        exit()

print('None')