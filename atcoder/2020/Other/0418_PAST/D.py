S = input()

# 文字列が1の場合
a1 = len(set(S)) + 1

# 文字列が2の場合
a2_set = {'..'}
for i in range(len(S)-1):
    a2_set.add(S[i]+S[i+1])
    a2_set.add(S[i]+'.')
    a2_set.add('.'+S[i+1])
a2 = len(a2_set)

# 文字列が3の場合
a3_set = {'...'}
for i in range(len(S)-2):
    a3_set.add(S[i]+S[i+1]+S[i+2])
    a3_set.add(S[i]+S[i+1]+'.')
    a3_set.add(S[i]+'.'+S[i+2])
    a3_set.add('.'+S[i+1]+S[i+2])
    a3_set.add(S[i]+'..')
    a3_set.add('..'+S[i+2])
    a3_set.add('.'+S[i+1]+'.')
a3 = len(a3_set)

if len(S)==1:
    print(a1)
elif len(S)==2:
    print(a1+a2)
else:
    print(a1+a2+a3)