s = input()
a, b = int(s[:2]), int(s[2:])

if 0<a<13 and 0<b<13:
    ans = 'AMBIGUOUS'
elif 0<a<13 and (b>12 or b==0):
    ans = 'MMYY'
elif (a>12 or a==0) and 0<b<13:
    ans = 'YYMM'
else:
    ans = 'NA'

print(ans)