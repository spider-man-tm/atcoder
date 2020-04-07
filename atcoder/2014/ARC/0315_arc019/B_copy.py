a = input()
l = len(a)
dif = 0
for i in range(l//2):
    if a[i]!=a[-i-1]:
        dif += 1
ans = 25*l
if dif==0 and l%2==1:
    ans -= 25
elif dif==1:
    ans -= 2
    
print(ans)