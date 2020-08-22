S = input()

count = S.count('R')

if count == 0 or count == 1 or count == 3:
    print(count)
else:
    if S == 'RSR':
        print(1)
    else:
        print(2)