n = int(input())
n_origin = n

s = 0
keta = 10

while n >= 1:
    s += n%10
    n //= keta

if n_origin%s==0:
    print('Yes')
else:
    print('No')