n = int(input())
st = ''

while n != 0:
    r = abs(n % 2)
    n = (n - r) // (-2)
    st += str(r)

tmp = list(reversed(list(st)))
ans = ''.join(tmp)
if st == '':
    print(0)
    exit()

print(ans)