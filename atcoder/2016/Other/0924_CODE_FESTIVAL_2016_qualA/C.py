s = input()
K = int(input())

S = [ord(i)-97 for i in s]

last = K
for i in range(len(S)):
    if S[i] != 0:
        if 26 - S[i] <= last:
            last -= 26 - S[i]
            S[i] = 0

if last > 0:
    S[-1] += last
    S[-1] %= 26

S = [chr(i+97) for i in S]
print(''.join(S))