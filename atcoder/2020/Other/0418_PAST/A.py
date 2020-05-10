S, T = input().split()

def func(s):
    if s[0] == 'B':
        return -1 * int(s[1])
    else:
        return int(s[0])

S = func(S)
T = func(T)

if S*T > 0:
    print(abs(T-S))
else:
    print(abs(T-S)-1)