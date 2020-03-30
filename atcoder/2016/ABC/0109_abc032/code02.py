s = input()
k = int(input())
ans = set()

for i in range(len(s)-k+1):
    moji = s[i:i+k]
    ans.add(moji)

print(len(ans))