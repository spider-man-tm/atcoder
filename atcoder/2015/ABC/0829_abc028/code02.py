s = input()
ans = [0, 0, 0, 0, 0, 0]

for i in s:
    ans[ord(i)-65] += 1

for i, an in enumerate(ans):
    if i!=5:
        print(an, end=' ')
    else:
        print(an)