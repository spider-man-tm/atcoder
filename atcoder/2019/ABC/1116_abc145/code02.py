n = int(input())
s = input()

if n%2==1:
    print('No')
    exit()

if s[:len(s)//2] == s[len(s)//2:]:
    print('Yes')
else:
    print('No')