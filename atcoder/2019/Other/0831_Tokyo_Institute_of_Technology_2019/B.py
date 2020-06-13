import re

N = int(input())

# .*は任意の文字列
pattern = re.compile('.*okyo.*ech.*')

for _ in range(N):
    S = input()
    if re.search(pattern, S):
        print('Yes')
    else:
        print('No')