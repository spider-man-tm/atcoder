s = input()
before = s[0]

ans = 'Good'

for i in range(1, 4):
    after = s[i]
    if before==after:
        ans = 'Bad'
    before = after

print(ans)