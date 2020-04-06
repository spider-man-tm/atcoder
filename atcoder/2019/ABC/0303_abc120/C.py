import re

s = input()

c0, c1 = 0, 0
for i in s:
    if i=='0':
        c0 += 1
    else:
        c1 += 1

print(min(c0, c1)*2)

"""TLE
def trans_word(text):
    replacements = {'01': '', '10': ''}
    return re.sub('({})'.format('|'.join(map(re.escape, replacements.keys()))), lambda m: replacements[m.group()], text)

ans = 0
flag = True

while flag:
    s_tmp = s
    s = trans_word(s)
    ans += (len(s_tmp) - len(s))
    flag = len(s_tmp) - len(s)

print(ans)
"""