N = int(input())
S = []

for _ in range(N):
    s = input()
    zero = 0
    for i in range(len(s)):
        if s[i] == '0':
            zero += 1
        else:
            break
    S.append([int(s), zero, s])

S = sorted(S, key=lambda x: x[1], reverse=True)
S = sorted(S, key=lambda x: x[0])

for i in range(N):
    print(S[i][2])