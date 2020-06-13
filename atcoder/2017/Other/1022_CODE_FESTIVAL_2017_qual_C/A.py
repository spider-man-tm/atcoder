import re

def pattern_match(s):
    pattern = re.compile('AC')
    return re.search(pattern, s)

if pattern_match(input()):
    print('Yes')
else:
    print('No')