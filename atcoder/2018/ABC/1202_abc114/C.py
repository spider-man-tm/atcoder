import itertools as itr

num = int(input())

a = ['0', '3', '5', '7']
b = ['0', '3', '5', '7']
c = ['0', '3', '5', '7']
d = ['0', '3', '5', '7']
e = ['0', '3', '5', '7']
f = ['0', '3', '5', '7']
g = ['0', '3', '5', '7']
h = ['0', '3', '5', '7']
i = ['0', '3', '5', '7']

cnt = 0
for j,k,l,m,n,o,p,q,r in itr.product(a,b,c,d,e,f,g,h,i):
    num2 = int(j+k+l+m+n+o+p+q+r)
    num2 = str(num2)
    if '0' not in num2:
        if '3' in num2 and '5' in num2 and '7' in num2:
            num2 = int(num2)
            if num >= num2:
                cnt += 1

print(cnt)