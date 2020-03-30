n = int(input())

w = []
for i in range(n):
    word = input()
    if i==0:
        before = word
    else:
        if before[-1] != word[0]:
            print('No')
            exit()
        else:
            before = word
    w.append(word)

if len(set(w)) != len(w):
    print('No')
    exit()

print('Yes')