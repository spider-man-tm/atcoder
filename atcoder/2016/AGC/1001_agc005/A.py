X = input()
s, t = 0, 0
for i in X:
    if i=='S':
        s += 1
    else:
        if s==0:
            t += 1
        else:
            s-= 1
print(s+t)