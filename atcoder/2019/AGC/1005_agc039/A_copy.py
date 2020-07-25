s = list(input())
k = int(input())

if list(s[0]*len(s))==s:
	#print('a')
	print(len(s)*k//2)
	exit()

res = [1]
for i in range(len(s)-1):
	if s[i]==s[i+1]:
		res[-1] += 1
	else:
		res.append(1)
ans = 0
for i in res:
	ans += (i//2)*k
if s[0]==s[-1]:
	diff = (res[0]+res[-1])//2 -(res[0]//2 + res[-1]//2)
	ans += diff*(k-1)
print(ans)
