s = input()
n = int(input())

s_list = sorted([s[0], s[1], s[2], s[3], s[4]])

cnt = 0
for i in range(5):
    for j in range(5):
        cnt += 1
        if cnt == n:
            print(s_list[i], s_list[j], sep='')