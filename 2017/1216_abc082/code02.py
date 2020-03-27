s = input()
t = input()

if s==t:
    print('No')
    exit()

s, t = [c for c in s], [c for c in t]
s = sorted(s)
t = sorted(t, reverse=True)

s = ''.join(s)
t = ''.join(t)

if [s, t]==sorted([s, t]):
    print('Yes')
else:
    print('No')