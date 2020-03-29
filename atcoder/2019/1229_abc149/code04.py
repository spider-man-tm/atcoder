n, k = map(int, input().split())
R, S, P = map(int, input().split())
t = input()

score = 0

for i in range(k):
    aa = t[i::k]
    before = ''
    for ja in aa:
        if ja==before:
            before = ''
            continue
        else:
            if ja=='s':
                score += R
            elif ja=='p':
                score += S
            else:
                score += P
            before = ja

print(score)