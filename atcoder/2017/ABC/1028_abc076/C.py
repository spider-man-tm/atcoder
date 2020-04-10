S = input()
T = input()

for i in range(len(S)-len(T)+1)[::-1]:
    tmp = S[i:i+len(T)]
    flag = True

    for j in range(len(T)):
        if tmp[j]!=T[j] and tmp[j]!='?':
            flag = False
            break

    if flag:
        w = S[:i] + T + S[i+len(T):]
        w = w.replace('?', 'a')
        print(w)
        exit()

print('UNRESTORABLE')