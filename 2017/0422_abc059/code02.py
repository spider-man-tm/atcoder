a = input()
b = input()
if len(a)>len(b):
    print('GREATER')
elif len(b)>len(a):
    print('LESS')
else:
    if int(a)>int(b):
        print('GREATER')
    elif int(b)>int(a):
        print('LESS')
    else:
        print('EQUAL')