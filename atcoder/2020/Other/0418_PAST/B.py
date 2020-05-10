S = input()
a, b, c = 0, 0, 0

for s in S:
    if s == "a":
        a += 1
    elif s == "b":
        b += 1
    else:
        c += 1

maxi = max(a, b, c)

if maxi==a:
    print('a')
elif maxi==b:
    print('b')
else:
    print('c')