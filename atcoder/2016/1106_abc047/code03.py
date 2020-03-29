S = input()

s = []
before = S[0]
for i in range(len(S)):
    if S[i] != before:
        s.append(before)
        before = S[i]
    
    if i == len(S)-1:
        s.append(S[i])

print(len(s)-1)