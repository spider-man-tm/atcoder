s = input()

mini = float('inf')
for i in range(len(s)-2):
    num = int(s[i])*100 + int(s[i+1])*10 + int(s[i+2])
    diff = abs(753 - num)

    if diff < mini:
        mini = diff

print(mini)