ss = input()

even, odd = [], []

for i, s in enumerate(ss):
    if i%2==1:
        even.append(s)
    else:
        odd.append(s)

if ('L' in odd) or ('R' in even):
    print('No')

else:
    print('Yes') 