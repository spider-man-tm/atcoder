Sa = input()
Sb = input()
Sc = input()

Sa = [c for c in Sa]
Sb = [c for c in Sb]
Sc = [c for c in Sc]

tmp = Sa.pop(0)

for _ in range(len(Sa)+len(Sb)+len(Sc)+1):
    if tmp == 'a':
        if len(Sa)==0:
            print('A')
            exit()
        else:
            tmp = Sa.pop(0)
    elif tmp == 'b':
        if len(Sb)==0:
            print('B')
            exit()
        else:
            tmp = Sb.pop(0)
    else:
        if len(Sc)==0:
            print('C')
            exit()
        else:
            tmp = Sc.pop(0)