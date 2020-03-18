s = input()
ans_list = [0] * 26

for i in s:
    i = ord(i) - 97
    ans_list[i] += 1

for i, s in enumerate(ans_list):
    if s==0:
        print(chr(i+97))
        exit()

print('None')