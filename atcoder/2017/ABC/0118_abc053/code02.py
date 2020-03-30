s = input()

for i in range(len(s)):
    if s[i]=='A':
        start=i
        break

for j in range(len(s)):
    if s[len(s)-1-j]=='Z':
        end=len(s)-1-j
        break

print(end-start+1)