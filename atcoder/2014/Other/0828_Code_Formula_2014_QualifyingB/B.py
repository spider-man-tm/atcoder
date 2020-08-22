N = input()[::-1]

odd, eve = 0, 0
for i in range(len(N)):
    if i % 2 == 0:
        odd += int(N[i])
    else:
        eve += int(N[i])

print(eve, odd)