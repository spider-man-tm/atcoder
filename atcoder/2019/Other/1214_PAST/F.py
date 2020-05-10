S = input()
word = []
tmp = []
flag = False

for c in S:
    if flag==False:
        flag = True
        tmp.append(c)
    elif flag:
        if c.islower():
            tmp.append(c)
        else:
            flag = False
            tmp.append(c)
            w = ''.join(tmp)
            word.append(w)
            tmp = []
word = sorted(word, key=str.lower)
print(*word, sep='')