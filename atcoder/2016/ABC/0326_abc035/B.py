s = input()
t = int(input())

dron = [0, 0]
hatena = 0

for i in s:
    if i == 'L':
        dron[0] -= 1
    elif i == 'R':
        dron[0] += 1
    elif i == 'U':
        dron[1] += 1
    elif i == 'D':
        dron[1] -= 1
    else:
        hatena += 1

if t == 1:
    dist = abs(dron[0]) + abs(dron[1]) + hatena
    print(dist)

else:
    dist = abs(dron[0]) + abs(dron[1]) - hatena
    
    if dist < 0:
        if dist % 2 == 0:
            dist = 0
        else:
            dist = 1
        
    print(dist)