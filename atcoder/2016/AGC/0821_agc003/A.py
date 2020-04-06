S = input()

n = 'N' in S
s = 'S' in S
e = 'E' in S
w = 'W' in S

if (n and s) or (n==False and s==False):
    if (e and w) or (e==False and w==False):
        print('Yes')
    else:
        print('No')
else:
    print('No')