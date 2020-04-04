s = input()
k = int(input())
strings = set()
for start in range(len(s)):
    for end in range(start+1, start+1+k):
        moji = s[start:end]
        strings.add(moji)

ans = sorted(list(strings))[k-1]
print(ans)