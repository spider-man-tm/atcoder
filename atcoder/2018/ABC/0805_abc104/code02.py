s = input()
if s[0]=='A':
    if s[2:-1].count('C')==1:
        s = s.replace('A', 'a').replace('C', 'c')
        if s.islower():
            print('AC')
            exit()

print('WA')