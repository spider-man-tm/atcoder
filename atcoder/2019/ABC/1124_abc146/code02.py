n = int(input())
s = input()

for ss in s:
    i = ord(ss)
    i += n
    if i>90:
        i -= 26
    ss = chr(i)
    print(ss, end='')