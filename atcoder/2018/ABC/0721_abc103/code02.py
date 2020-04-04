S = input()
T = input()

for i in range(len(S)):
    tmp = S[(-1*i):] + S[:(-1*i)]
    if tmp==T:
        print('Yes')
        exit()

print('No')