S = input()
l = [0]*(len(S)+1)

for i in range(len(S)):
    if S[i] == '<':
        l[i+1] = l[i]+1

l = l[::-1]
S = S[::-1]

for i in range(len(S)):
    if S[i] == '>':
        l[i+1] = max(l[i]+1, l[i+1])

print(sum(l))