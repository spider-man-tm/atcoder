s = input()
s = [c for c in s]
leng = len(s)
s = set(s)
if leng==len(s):
    print('yes')
else:
    print('no')