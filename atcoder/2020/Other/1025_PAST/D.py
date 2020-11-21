N = int(input())
S = input()

cnt, maxi = 0, 0
for i in range(N):
    if S[i] == '.':
        cnt += 1
    else:
        cnt = 0
    maxi = max(maxi, cnt)

left = 0
i = 0
while S[i] == '.':
    left += 1
    i += 1

right = 0
i = 1
while S[-i] == '.':
    right += 1
    i += 1


if left + right >= maxi:
    print(left, right)
else:
    tmp = maxi - (left + right)
    print(left+tmp, right)
