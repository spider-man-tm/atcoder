A, B = map(int, input().split())
S = input()

if len(S) != A+B+1:
    print('No')
    exit()

try:
    int(S[:A])
except ValueError:
    print('No')
    exit()

if S[A]!='-':
    print('No')
    exit()

try:
    int(S[A+1:])
except ValueError:
    print('No')
    exit()

print('Yes')