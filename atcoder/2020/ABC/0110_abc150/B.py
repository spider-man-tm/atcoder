n = int(input())
s = input()

count = 0
for i in range(1, len(s)-1):
    if s[i-1]=='A' and s[i]=='B' and s[i+1]=='C':
        count += 1
    else:
        pass

print(count)